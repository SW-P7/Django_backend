from typing import Any
from django.db import models
import uuid

class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    software_version = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    ip_addr = models.GenericIPAddressField(null=True)
    ping = models.IntegerField(null=True)
    last_online = models.DateTimeField(null=True)

    class Meta:
        verbose_name = "device"
        verbose_name_plural = "devices"

    
class UpdateLogs(models.Model):
    id = models.UUIDField(name='id', null=False, unique=True, primary_key=True, default=uuid.uuid4())
    device = models.ForeignKey(Device, on_delete=models.PROTECT, default=None)
    log_location = models.CharField(name='update log', null=False, default="/home/user/logs")
    name = models.CharField(name="name", null=False, default="gib name plzz")
     
    class Meta:
        verbose_name = "updatelog"
        verbose_name_plural = "updatelogs"
