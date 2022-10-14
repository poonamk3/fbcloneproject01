from rest_framework import serializers
from django.contrib.auth.models import User 
from login.models import Post
from login.utilis import Util
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.mixins import ListModelMixin
from rest_framework.validators import UniqueValidator
from django.core.validators import EmailValidator


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
        
    def validate(self, attrs):
        email = attrs.get('email')
        body = 'You are register from fbclone project'
        data = {
        'subject':'Fbclone Project',
        'body':body,
        'to_email':email
        }
        Util.send_email(data)
        return attrs
    
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=True, style={"input_type": "password"})
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    # email=serializers.EmailField(required=True)
    class Meta:
        model = User
        fields = ["email","username", "password"]
        extra_kwargs = {
        'email': {'validators': [EmailValidator,]},
        }

    

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields = ["id","title", "image","description","author"]


class UserSerializer(serializers.ModelSerializer):
    postuser = serializers.StringRelatedField(many=True)
    class Meta:
        model=User
        fields= ['username','password','likes','postuser']