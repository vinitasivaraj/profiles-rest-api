from rest_framework import serializers
from .models import UserProfile

class HelloSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=10)