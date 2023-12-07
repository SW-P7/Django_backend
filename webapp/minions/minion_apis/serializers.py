from rest_framework import serializers
from ..models import Device

class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'

class PingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ['ping', 'software_version']


class UpdateSerializer(serializers.Serializer):
    update_id = serializers.UUIDField()
    device_id = serializers.UUIDField()   
