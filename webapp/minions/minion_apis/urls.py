from django.urls import path
from webapp.minions.minion_apis.views import MinionListCreate, MinionRetrieveUpdateDestroy, DeviceViewSets, DeviceGetPing

#Legacy
urlpatterns = [
    #path('minions/', MinionListCreate.as_view(), name='minion-list-create'),
    path('minions/<int:pk>/', MinionRetrieveUpdateDestroy.as_view(), name='minion-retrieve-update-destroy'),
    path('minions/', DeviceViewSets.as_view() , name='retrieve_device'),
    path('minions/ping/<int:pk>/', DeviceGetPing, name='retrieve_device_ping'),
    
]
