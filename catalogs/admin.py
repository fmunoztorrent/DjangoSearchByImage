from django.contrib import admin
from .models import Catalog, CatalogProduct, CatalogImage


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    search_fields = ['name','client']
    list_display = ('name','client')


class CatalogImageAdmin(admin.TabularInline):
    model = CatalogImage
    extra = 0


@admin.register(CatalogProduct)
class CatalogProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    search_fields = ['catalog','name','link','date_created']
    list_display = ('catalog','name','link','date_created')
    inlines = [CatalogImageAdmin]
