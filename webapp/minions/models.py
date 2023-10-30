from django.db import models


class Device(models.Model):
    id = models.UUIDField(name='id', null=False, unique=True, primary_key=True)
    software_version = models.FloatField(name='software version', null=True)
    
class UpdateLogs(models.Model):
    id = models.UUIDField(name='id', null=False, unique=True, primary_key=True)
    device = models.ManyToOneRel(field=Device.id ,to=Device,field_name='id' ,on_delete=models.PROTECT)
    log = models.CharField( name='update log', null=False)