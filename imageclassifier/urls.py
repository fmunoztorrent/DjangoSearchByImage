from django.urls import path
from .views import ClientCatalogImageClassifierView

urlpatterns = [
    path('', ClientCatalogImageClassifierView.as_view(), name='imageclasifier'),
]