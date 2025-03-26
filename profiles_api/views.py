from rest_framework.views import APIView
from rest_framework.response import Response


class HelooApi(APIView):

    def get(self,request,format=None):
        an_apiview=[
            "uses Http method",'is similar to django view','is mapped manually',
        ]
        return Response({'message':"Hello",'an_apiview':an_apiview})
