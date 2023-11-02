from django.urls import path
from webapp.states.state_apis.views import StateCreate

urlpatterns = [
    path('states/', StateCreate.as_view(), name='state-create'),
    #path('states/<int:pk>/', MinionRetrieveUpdateDestroy.as_view(), name='minion-retrieve-update-destroy'),
    #path('states/<uuid:id>/',DeviceLookupView.as_view() , name='retrieve_device')
]
