from django.db import models


class SoftwareState(models.Model):
    id = models.UUIDField(name='id', unique=True, null=False, primary_key=True)
    software_update = models.JSONField(name="software update", null=True)
    code_update = models.JSONField(null=True, editable=True)
    version = models.CharField(verbose_name="version number", null=False, default="")
    
    class Meta:
        verbose_name="software state"
        verbose_name_plural="software states"
    
    
    
    