from uuid import UUID, uuid4

from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework import generics, viewsets, mixins, request, status
from rest_framework.schemas.coreapi import serializers
from webapp.states.models import Update

from webapp.decorators import register_viewset
from webapp.minions.models import Device
from webapp.states.models import SoftwareState
from webapp.minions.minion_apis.serializers import DeviceSerializer, PingSerializer, UpdateSerializer, UpdateLogSerializer
from rest_framework.decorators import action
from django.http import HttpResponse
from django.utils import timezone
from ftplib import FTP

import socket
import time
import http.client
import datetime

import logging

logger = logging.getLogger(__name__)

router = DefaultRouter()

@register_viewset(router=router, prefix='devices', basename='device')
class DeviceViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    def get_serializer_class(self):
        if self.action == 'send_update':
            return UpdateSerializer
        else:
            return DeviceSerializer
    #def         
    queryset = Device.objects.all()

    @action(detail=True, methods=['get'], url_path='get_status')
    def get_status(self, request, pk=None):
        # Your logic to get ping for the specified device
        # Replace the following line with your actual logic
        device = self.get_object()
        if ping_device(device):
            data = PingSerializer(device).data
            return Response(data, status=200)
        return Response(status = 500)

    @action(detail=True, methods=['post'], url_path='send_update', serializer_class=UpdateSerializer)
    def send_update(self, request, pk=None):        
        serializer = UpdateSerializer(data=request.data)
        if not serializer.is_valid():
            logger.warning("data is not valid UUID")
            return Response(f"{request.data}", status=status.HTTP_400_BAD_REQUEST)
        update_id = serializer.validated_data['update_id_list']
        device_id = serializer.validated_data['device_id_list']

        update_dict = {}
        try:
            for id in device_id:
                device = Device.objects.get(id=id)
                conn = http.client.HTTPConnection(device.ip_addr, 5000, timeout=2)
                logger.debug(device.ip_addr)
                for uid in update_id:
                    update = SoftwareState.objects.get(id=uid)
                    conn.request("POST", "/update", body=update.state ,headers={"Host": device.ip_addr, "Name": update.name})
                    if conn.getresponse().getcode() == 200:
                        logger.info(f"success update request to device {device_id} with update {update_id}")
                        if "success" not in update_dict:
                            update_dict.update({"success": [{id : uid}]})
                            Update.objects.create(id=uuid4(), device=Device.objects.get(id=id), softwarestate=SoftwareState.objects.get())
                        else:
                            Update.objects.create(id=uuid4(), device=Device.objects.get(id=id), softwarestate=SoftwareState.objects.get()) 
                            update_dict["success"].append({id : uid})
                        #return Response("success", status=status.HTTP_200_OK)
                    else:
                        logger.warning(f"unsuccessfull update request to device {device_id}, with update {update_id}")
                        if "failure" not in update_dict:
                            update_dict.update({"failure": [{id : uid}]})
                        else:
                            update_dict["failure"].append({id : uid})
            return Response(str(update_dict), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e.__str__(), status=status.HTTP_504_GATEWAY_TIMEOUT)

    @action(detail=True, methods=['get'], url_path='logs', serializer_class=None) 
    def upload_create_logs(self, request, pk=None):
        serializer = UpdateLogSerializer(data=request.data)
        if not serializer.is_valid():
            logger.info("incorrect device_id")
            return Response("incorrect device_id", status=status.HTTP_400_BAD_REQUEST)
        


        device_id = serializer.validated_data['device_id']
        device = Device.objects.filter(id=device_id).first()
        if device is None:
            raise Exception("device not found")
        try:
            conn = http.client.HTTPConnection(device.ip_addr, 5000, timeout=2)
            logger.info(f"connected to device {device.ip_addr}")
            conn.request("GET", "/logs", headers={"Host": device.ip_addr})
            
            res = conn.getresponse()
            logs_non_split : str = res.read().decode()  
            conn.send("success")
                    
        except Exception as e:
            return Response("Connection timeout", status.HTTP_504_GATEWAY_TIMEOUT)
        
        logs : list = logs_non_split.split(".log:")
        #Implement FTP Server Connection here :)



def ping_device(device: Device):
    conn = http.client.HTTPConnection(device.ip_addr, 5000, timeout=10)
    time_before = time.time()
    try:
        conn.request("GET", "/ping", headers={"Host": device.ip_addr})
        ping = round((time.time() - time_before) * 1000)
        if conn.getresponse().getcode() == 200:
            device.last_online = timezone.now()
            device.ping = ping
            device.save()
            return True
    except Exception:
        return False
    return False

def tcp_ping_device(device):
    host = '172.17.0.1'
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = "ping"
    data = ""
    time_before = time.time()
    
    while data != 'done':
        client_socket.sendall(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        if data == "pong":
            time_after = time.time()
            message = "recieved"
        if data == "version?" and device.software_version != None:
            message = device.software_version
        if data == "version?" and device.software_version == None:
            message = "1.0.0"
        if data == "version!":
            client_socket.sendall(str.encode("ready"))
            version = client_socket.recv(1024).decode()
            device.software_version = version
            message = "done"
    client_socket.close()  # close the connection
     
    ping = round((time_after - time_before) * 1000)
    device.ping = ping
    device.save()

    return True

# class MinionListCreate(generics.ListCreateAPIView):
    # queryset = Device.objects.all()
#     serializer_class = DeviceSerializer

# class MinionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Device.objects.all()
    # serializer_class = DeviceSerializer

