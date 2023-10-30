from django.db import models


class Device(models.Model):
    id = models.UUIDField(name='id', null=False, unique=True, primary_key=True)
    software_version = models.FloatField(name='software version', null=True)
    
