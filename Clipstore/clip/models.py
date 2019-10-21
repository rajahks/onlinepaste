from django.db import models
# from datetime import datetime, timezone
from django.utils import timezone

# Create your models here.
class Clip(models.Model):
    clipId = models.CharField(max_length=20)
    clipText = models.TextField()
    # the below date time fields are timezone aware with timezone as utc.
    create_date = models.DateTimeField(default=timezone.now,editable=False)
    expiry_date = models.DateTimeField(default=timezone.now) #set based on value chosen by user.
    #datetime.now(timezone.utc)
    link_expire_options = (
                            ( 0, "On Access"),
                            ( 1, "1 hr"),
                            ( 24, "1 day"),
                            ( 240, "10 days"),
                            ( 480, "20 days"),
                            ( 720, "30 days")
                         )
    link_duration = models.IntegerField(choices=link_expire_options,default=0)

    isEncrypted = models.BooleanField(default=False)
    encryptedUrl = models.TextField(blank=True,default=None)

    def __str__(self):
        return self.clipId
