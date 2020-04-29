from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    search_fields = ['name','user']
    list_display = ('name','user')
