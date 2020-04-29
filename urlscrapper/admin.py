from django.contrib import admin
from .models import ScrapedBox

@admin.register(ScrapedBox)
class ScrapedBoxAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    search_fields = ['name','catalog','link']
    list_display = ('name','catalog','link')

