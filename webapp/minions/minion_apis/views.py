from uuid import UUID

from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework import generics, viewsets, mixins

from webapp.decorators import register_viewset
from webapp.minions.models import Device
from webapp.minions.minion_apis.serializers import DeviceSerializer
from rest_framework.decorators import action

import socket
import time

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
        ping_result = ping_device(device.ip_addr)
        return Response({'ping': ping_result})

def ping_device(host: str):
    host = '172.17.0.1'
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = "ping"
    data = ""
    time_before = time.time()
    
    while data != 'pong':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
    
    time_after = time.time()
    client_socket.close()  # close the connection
    
    ping = round((time_after - time_before) * 1000)
    
    return ping

# class MinionListCreate(generics.ListCreateAPIView):
    # queryset = Device.objects.all()
#     serializer_class = DeviceSerializer

# class MinionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Device.objects.all()
    # serializer_class = DeviceSerializer

