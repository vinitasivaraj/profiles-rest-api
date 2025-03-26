from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from.serializers import HelloSerializers,UserProfileSerializer
from .models import UserProfile
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .permissions import UpdateownPermission
from rest_framework import filters
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
    
class HelloViewset(viewsets.ViewSet):
    serializer_class=HelloSerializers
    def list(self,request):
        a_viewset={
            "its insede view sets"
        }
        return Response({"a_viewset":a_viewset})
    
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message":message})
        else:
            return Response(serializer.errors,status=status.http_400_BAD_REQUEST)
        

class UserProfileviewset(viewsets.ModelViewSet):
    serializer_class=UserProfileSerializer
    queryset=UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(UpdateownPermission,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)

class UserloginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


