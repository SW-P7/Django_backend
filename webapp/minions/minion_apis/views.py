from rest_framework.response import Response
from rest_framework import generics
from webapp.minions.models import Device
from webapp.minions.minion_apis.serializers import DeviceSerializer
from uuid import UUID

class MinionListCreate(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class MinionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    
class DeviceLookupView(generics.RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        id = UUID(str(self.kwargs.get('id')))
        device = Device.objects.filter(id=id).first()
        serializer_class = DeviceSerializer(device) 
        return Response(serializer_class.data, status=200)
   