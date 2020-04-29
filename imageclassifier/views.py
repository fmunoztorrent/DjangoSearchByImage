from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from urlscrapper.models import ScrapedBox
from catalogs.models import Catalog, CatalogProduct, CatalogImage
import json


# App Custom Modules import
from modules.ImageClassifer.ImageClassifier import ImageClassifier


class VisitorSearchByImageView(APIView):
    
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [JSONRenderer]

    def post(self, request):
        pass





class ClientCatalogImageClassifierView(APIView):

    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [JSONRenderer]

    def post(self,request):
        
        payload = json.loads( request.body.decode('utf-8') )
        scrapped_box_id = payload.get('id', None)

        if not scrapped_box_id:
            return Response({
                "error" : True,
                "detail" : "Box id not exists"
            })


        # Select Scrapped box
        try:
            box = ScrapedBox.objects.get(id=scrapped_box_id)

            if box.procesed:
                raise Exception("This scraped box is already procesed")

        except Exception as error:
            api_response = {"error" : True, "detail" : str(error)}

        else:

            ImageClassificator = ImageClassifier(box.image_url)
            image_classification = ImageClassificator.image_data()

            # Save response ...
            try:

                # New Product
                a_new_product = CatalogProduct()
                a_new_product.catalog = box.catalog
                a_new_product.name = box.name
                a_new_product.link = box.link
                a_new_product.save()

                # Associate image to product
                a_image_for_a_product = CatalogImage()
                a_image_for_a_product.product = a_new_product
                a_image_for_a_product.image_url = box.image_url
                a_image_for_a_product.image_data = image_classification
                a_image_for_a_product.save()
                

            except Exception as error:
                api_response = {"error" : True, "detail" : str(error)}

            else:

                box.procesed = True
                box.save()

                api_response = {
                    "error" : False,
                    "detail" : "Image succesfully classified",
                    "classification_result" : image_classification,
                }

            
        return Response(api_response)