from django.db import models


class SoftwareState(models.Model):
    id = models.UUIDField(name='id', unique=True, null=False, primary_key=True)
    state = models.CharField(verbose_name="software state", null=False, default="")
    
    class Meta:
        verbose_name="software state"
        verbose_name_plural="software states"
    
    
    
    
