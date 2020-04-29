from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from urlscrapper.models import ScrapedBox
from catalogs.models import Catalog, CatalogProduct, CatalogImage
from imageupload.models import UploadedImage
from django.conf import settings
import json


# App Custom Modules import
from modules.ImageClassifer.ImageClassifier import ImageClassifier


class VisitorSearchByImageView(APIView):
    
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [JSONRenderer]

    def get(self, request, image_id):

        image_file = UploadedImage.objects.get(pk=image_id)

        if image_file.procesed:
            data = image_file.image_data

        else:
            a_new_image_classification = ImageClassifier(image_file.image_file.path,'filesystem')
            data = a_new_image_classification.image_data()
            image_file.image_data = data
            image_file.procesed = True
            image_file.save()

        
        # Select clien catalogs
        client_catalogs = list(Catalog.objects.filter(client=image_file.client))

        # Select products from client's catalogs
        client_products = list(CatalogProduct.objects.filter(catalog__in=client_catalogs))

        # Select images for products
        product_images = CatalogImage.objects.filter(product__in=client_products)



        matched_images = []
        for product_image in product_images:

            for entity in product_image.image_data["entities"]:    
                for uploaded_image_entity in data["entities"]:
                    if uploaded_image_entity["description"] == entity["description"]:
                        matched_images.append(product_image)

        

        group_repeatings = {}
        for image in matched_images:

            if not group_repeatings.get(image.product.id,None):
                group_repeatings[image.product.id] = {
                    "repeating" : 1,
                    "name" : image.product.name,
                    "link" : image.product.link,
                    "image_url" : image.image_url,
                }

            else:
                group_repeatings[image.product.id]["repeating"] += 1



        search_result = []
        for key, result in group_repeatings.items():
            search_result.append(result)

        ordered_search_result = sorted(search_result, key=lambda k: k['repeating'])

        return Response(ordered_search_result)