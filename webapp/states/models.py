from django.db import models
from rest_framework.serializers import CharField

class SoftwareState(models.Model):
    id = models.UUIDField(name='id', unique=True, null=False, primary_key=True)
    state = models.TextField(verbose_name="software state", null=True, default="")
    name = models.CharField(name="name", null=False, default="gib me name plz")
    class Meta:
        verbose_name="software state"
        verbose_name_plural="software states"
    
    
    
    
