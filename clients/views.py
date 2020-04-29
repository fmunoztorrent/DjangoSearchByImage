from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.views import APIView

# Catalog CRUD
class ClientView(APIView):

    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [JSONRenderer]


    def get(self,request, id=None):
        """ Catalog listing & detail """
        pass