from rest_framework import serializers
#from rest_framework.fields import ListField
from ..models import Device
from drf_compound_fields.fields import ListField 

class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'

class PingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ['ping', 'software_version']


class UpdateSerializer(serializers.Serializer):
    update_id_list = ListField(child=serializers.UUIDField())
    device_id_list= ListField(child=serializers.UUIDField())   
