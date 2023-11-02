from django.urls import path
from webapp.minions.minion_apis.views import MinionListCreate, MinionRetrieveUpdateDestroy, DeviceLookupView

urlpatterns = [
    path('minions/', MinionListCreate.as_view(), name='minion-list-create'),
    path('minions/<int:pk>/', MinionRetrieveUpdateDestroy.as_view(), name='minion-retrieve-update-destroy'),
    path('minions/<uuid:id>/',DeviceLookupView.as_view() , name='retrieve_device')
]
