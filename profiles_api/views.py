from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.serializers import HelloSerializers

class HelooApi(APIView):
    serializer_class=HelloSerializers


    def get(self,request,format=None):
        an_apiview=[
            "uses Http method",'is similar to django view','is mapped manually',
        ]
        return Response({'message':"Hello",'an_apiview':an_apiview})
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f"hello: {name}"
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.http_400_BAD_REQUEST)
        
    
    def put(self,request,pk=None):
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        return Response({'method':'delete'})


