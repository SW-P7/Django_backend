from django.db import models


class Device(models.Model):
    id = models.UUIDField(name='id', null=False, unique=True, primary_key=True)
    
