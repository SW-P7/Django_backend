from rest_framework import serializers
from ..models import SoftwareState

class StateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SoftwareState
        fields = '__all__'
