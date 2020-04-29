from django.db import models
from clients.models import Client
from jsonfield import JSONField
from django.utils import timezone

class Catalog(models.Model):

    client = models.ForeignKey( Client, on_delete = models.PROTECT, null = True )
    name = models.CharField(max_length=40)
    base_url = models.TextField()
    box_selector = models.TextField()
    box_title_selector = models.TextField()
    date_created = models.DateTimeField( default = timezone.now )

    def __str__(self):
        return self.name



class CatalogProduct(models.Model):

    catalog = models.ForeignKey( Catalog, on_delete = models.PROTECT, null = True )
    name = models.CharField(max_length=100)
    link = models.TextField()
    date_created = models.DateTimeField( default = timezone.now )

    def __str__(self):
        return self.name



class CatalogImage(models.Model):

    product = models.ForeignKey( CatalogProduct, on_delete = models.PROTECT, null = True )
    image_url = models.CharField(max_length=40)
    image_data = JSONField()

    def __str__(self):
        return self.product.name
    