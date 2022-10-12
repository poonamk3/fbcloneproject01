from rest_framework import serializers
from django.contrib.auth.models import User 
from login.models import Post
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields =  '__all__'
        # fields =  ['username','email','password','first_name']
        fields =  ['id','username','email','password','first_name']
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            email=validated_data['email'],


        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=True, style={"input_type": "password"})
    class Meta:
        model = User
        fields = ["username", "password"]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields = ["id","title", "image","description","author"]