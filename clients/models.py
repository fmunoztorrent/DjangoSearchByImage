from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Client(models.Model):

    user = models.ForeignKey( User, on_delete = models.PROTECT, null = True )
    name = models.CharField(max_length=40)
    date_created = models.DateTimeField( default = timezone.now )

    def __str__(self):
        return self.name