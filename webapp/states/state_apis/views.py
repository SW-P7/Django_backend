from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.routers import DefaultRouter

from webapp.states.models import SoftwareState
from webapp.states.state_apis.serializers import StateSerializer
from webapp.decorators import register_viewset

from uuid import UUID

router = DefaultRouter()

@register_viewset(router=router, prefix='states', basename='state')
class StateViewSet(viewsets.ModelViewSet):
    queryset = SoftwareState.objects.all()
    serializer_class = StateSerializer


class StateCreate(generics.ListCreateAPIView):
    queryset = SoftwareState.objects.all()
    serializer_class = StateSerializer
    
class StateRetrieve(generics.RetrieveAPIView):
    queryset = SoftwareState.objects.all()
    serializer_class = StateSerializer