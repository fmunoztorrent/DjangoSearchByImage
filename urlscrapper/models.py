from django.db import models
from catalogs.models import Catalog
from django.utils import timezone

class ScrapedBox(models.Model):

    catalog = models.ForeignKey( Catalog, on_delete = models.PROTECT, null = True )
    name = models.CharField(max_length=100)
    link = models.TextField()
    image_url = models.TextField()
    procesed = models.BooleanField(default=False)
    date_created = models.DateTimeField( default = timezone.now )

    def __str__(self):
        return self.name