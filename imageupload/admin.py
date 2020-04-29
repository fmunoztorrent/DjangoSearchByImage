from django.contrib import admin
from .models import UploadedImage

@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    search_fields = ['client','image_file']
    list_display = ('client','image_file')