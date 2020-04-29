from django.db import models
from clients.models import Client
from jsonfield import JSONField
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.utils import timezone

class UploadedImage(models.Model):

    client = models.ForeignKey( Client, on_delete = models.PROTECT, null = True )
    image_file = models.FileField(upload_to=settings.UPLOAD_IMAGE_STORAGE_REL)
    image_data = JSONField()
    procesed = models.BooleanField(default=False)
    date_created = models.DateTimeField( default = timezone.now )

    def __str__(self):
        return str(self.image_file)