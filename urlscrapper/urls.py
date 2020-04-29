from django.urls import path
from .views import UrlCrapperView

urlpatterns = [
    path('', UrlCrapperView.as_view(), name='urlscrapper'),
]