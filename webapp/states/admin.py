from django.contrib import admin
from webapp.states.models import Update
from webapp.states.models import SoftwareState 

admin.site.register(SoftwareState)
admin.site.register(Update)
