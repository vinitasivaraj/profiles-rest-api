from rest_framework import serializers
from .models import UserProfile

class HelloSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=('id','email','name','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':"password"}
            }
        }

    def create(self,validate_data):
        user=UserProfile.objects.create_user(
            email=validate_data['email'],
            name=validate_data['name'],
            password=validate_data['password']

        )
        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


