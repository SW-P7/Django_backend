from rest_framework.response import Response
from rest_framework import generics
from webapp.states.models import SoftwareState
from webapp.states.state_apis.serializers import StateSerializer
from uuid import UUID

class StateCreate(generics.ListCreateAPIView):
    queryset = SoftwareState.objects.all()
    serializer_class = StateSerializer
    
class StateRetrieve(generics.RetrieveAPIView):
    queryset = SoftwareState.objects.all()
    serializer_class = StateSerializer