from rest_framework import generics
from webapp.minions.models import Device
from webapp.minions.minion_apis.serializers import DeviceSerializer

class MinionListCreate(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class MinionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    
class DeviceLookupView(generics.RetrieveAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = 'name'
