from rest_framework import serializers
from ..models import SoftwareState

class StateSerializer(serializers.ModelSerializer):
    # Make this reflect the finished implementation of how states look
    # Create a seperate for inserting with checks on field values
    #
    
    class Meta:
        model = SoftwareState
        fields = '__all__'
