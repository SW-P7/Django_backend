from django.db import models
from rest_framework.serializers import CharField
from webapp.minions.models import Device

class SoftwareState(models.Model):
    id = models.UUIDField(name='id', unique=True, null=False, primary_key=True)
    state = models.TextField(verbose_name="software state", null=True, default="")
    name = models.CharField(name="name", null=False, default="gib me name plz")
    class Meta:
        verbose_name="software state"
        verbose_name_plural="software states"
    
class Update(models.Model):
    id = models.UUIDField(name='id', unique=True, null=False, primary_key=True)
    softwarestate = models.ForeignKey(SoftwareState,null=False, blank=False, on_delete=models.PROTECT)
    device = models.ForeignKey(Device,null=False, blank=False, on_delete=models.PROTECT)
