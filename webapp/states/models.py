from django.db import models


class SoftwareState(models.Model):
    id = models.UUIDField(name='id', unique=True, null=False, primary_key=True)
    code_update = models.JSONField()
    package_update = models.JSONField()
    
    