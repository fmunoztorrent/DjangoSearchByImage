from django import forms
from .models import UploadedImage


class ImageFileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ('client','image_file',)