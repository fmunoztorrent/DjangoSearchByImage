from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.views import APIView

# Catalog CRUD
class CatalogView(APIView):

    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [JSONRenderer]


    def get(self,request, id=None):
        """ Catalog listing & detail """
        pass


    def post(self,request):
        """ New Catalog """

        payload = json.loads( request.body.decode('utf-8') )

        url = payload.get('url', None)
        css_box_selector = payload.get('css_box_selector', None)
        css_box_title_selector = payload.get('css_box_title_selector', None)

        if not url or not css_box_selector or not css_box_title_selector:
            return Response({
                "error" : True,
                "detail" : "missing parameters"
            })
