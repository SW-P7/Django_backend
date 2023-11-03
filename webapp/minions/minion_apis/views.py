from uuid import UUID

from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework import generics, viewsets, mixins

from webapp.decorators import register_viewset
from webapp.minions.models import Device
from webapp.minions.minion_apis.serializers import DeviceSerializer



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



# class MinionListCreate(generics.ListCreateAPIView):
    # queryset = Device.objects.all()
#     serializer_class = DeviceSerializer

# class MinionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Device.objects.all()
    # serializer_class = DeviceSerializer

