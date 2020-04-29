from django.urls import path
from .views import VisitorSearchByImageView

urlpatterns = [
    path('', VisitorSearchByImageView.as_view(), name='imagesearcher'),
]