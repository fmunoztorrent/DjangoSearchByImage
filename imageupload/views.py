from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageFileUploadForm
from django.views import View
from braces.views import CsrfExemptMixin
from django.core.serializers.json import DjangoJSONEncoder
import json



class UploadImageView(CsrfExemptMixin, View):


    def get(self, request):
        form = ImageFileUploadForm()
        return render(request, 'image_upload_ajax.html', {'form': form})


    def post(self, request):

        form = ImageFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            a_new_image = form.save()
            response = {'error': False, 'message': 'Uploaded Successfully', "id" : a_new_image.pk}
        else:
            response = {'error': True, 'errors': form.errors}

        return HttpResponse( json.dumps( response,  cls=DjangoJSONEncoder ), content_type="application/json" )