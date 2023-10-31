from django.urls import path
from webapp.minions.minion_apis.views import MinionListCreate, MinionRetrieveUpdateDestroy

urlpatterns = [
    path('minions/', MinionListCreate.as_view(), name='minion-list-create'),
    path('minions/<int:pk>/', MinionRetrieveUpdateDestroy.as_view(), name='minion-retrieve-update-destroy'),
]
