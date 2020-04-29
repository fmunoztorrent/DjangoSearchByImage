from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.views import APIView
import json
from .models import ScrapedBox
from catalogs.models import Catalog

# Web Scrapper Imports
from modules.WebScrapper.ProductLinkList import ScrapCatalogProductBoxes, ProductCatalogBoxAssetExtractor, UrlDomainExtractor

# Catalog CRUD
class UrlCrapperView(APIView):

    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [JSONRenderer]


    def post(self,request):
        """ New URL to Scrap """

        try:

            payload = json.loads( request.body.decode('utf-8') )
            catalog_id = payload.get('catalog_id', None)
            baseurl = payload.get('baseurl', None)
            css_box_selector = payload.get('css_box_selector', None)
            css_box_title_selector = payload.get('css_box_title_selector', None)


        except Exception as error:
            
            return Response({
                "error" : True,
                "detail" : "missing parameters from catalog",
                "execpt" :  str(error),
            })

        else:


            if not baseurl or not css_box_selector or not css_box_title_selector:

                # Some of the above data is missing
                return Response({
                    "error" : True,
                    "detail" : "missing parameters from catalog"
                })


            # Move to a use case
            results = []
            Scrapper = ScrapCatalogProductBoxes(payload["baseurl"], payload["css_box_selector"])

            for box in Scrapper.result():

                # Domain FQDN
                site_domain = UrlDomainExtractor(payload["baseurl"])
                
                # Assets of interest
                Assets = ProductCatalogBoxAssetExtractor( box, site_domain.get_domain() )

                results.append({
                    "image_url" : Assets.image(),
                    "name" : Assets.name( payload["css_box_title_selector"] ),
                    "link" : Assets.link(),
                })


                # Insert new scrapped box to post processesing
                item_name = Assets.name( payload["css_box_title_selector"] )
                item_image = Assets.image()
                item_link = Assets.link()

                catalog = Catalog.objects.get(id=catalog_id)
                a_new_box = ScrapedBox(catalog=catalog, name=item_name, link=item_link, image_url=item_image)
                a_new_box.save()


            return Response(results)
