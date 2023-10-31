from django.db import models


class SoftwareState(models.Model):
    def __init__(self,) -> None:
        super(SoftwareState, self).__init__()
    id = models.UUIDField(name='id', unique=True, null=False, primary_key=True)
    software_update = models.JSONField(name="software updates", null=True),
    code_update = models.JSONField(name="software updates", null=True)
    
    