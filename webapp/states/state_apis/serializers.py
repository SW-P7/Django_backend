from rest_framework import serializers
from ..models import SoftwareState
import yaml
import logging
import json


logging = logging.getLogger(__name__)

class StateSerializer(serializers.ModelSerializer):
    # Make this reflect the finished implementation of how states look
    # Create a seperate for inserting with checks on field values
    
    class Meta:
        model = SoftwareState
        fields = '__all__'

    def validate_state(self, state):
        
        logging.debug("Entering State Validator")
        try:
            yaml.safe_load(state)
        except yaml.YAMLError as e:
            raise serializers.ValidationError("invalid yaml format" + str(e))
        #state = json.dumps(state)
        return state

