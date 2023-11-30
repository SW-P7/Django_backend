from uuid import UUID

from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework import generics, viewsets, mixins

from webapp.decorators import register_viewset
from webapp.minions.models import Device
from webapp.minions.minion_apis.serializers import DeviceSerializer, PingSerializer
from rest_framework.decorators import action
from django.http import HttpResponse
from django.utils import timezone

import socket
import time
import http.client
import datetime


router = DefaultRouter()

@register_viewset(router=router, prefix='devices', basename='device')
class DeviceViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DeviceSerializer
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

def ping_device(device: Device):
    conn = http.client.HTTPConnection(device.ip_addr, 5000)
    time_before = time.time()
    conn.request("GET", "/ping", headers={"Host": device.ip_addr})
    ping = round((time.time() - time_before) * 1000)
    if conn.getresponse().getcode() == 200:
        device.last_online = timezone.now()
        device.ping = ping
        device.save()
        return True
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

