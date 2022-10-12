from rest_framework import viewsets
from login.serializers import RegisterSerializer,LoginSerializer,PostSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate, login,logout
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from login.models import Post

class PostApi(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class registreviewapi(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = RegisterSerializer
	
	
class registreviewapis(generics.CreateAPIView):
	   queryset = User.objects.all()
	   serializer_class = RegisterSerializer


class LoginApi(APIView):
	queryset = User.objects.all()
	serializer_class = LoginSerializer
	def post(self, request,format=None):
		username=request.data['username']
		password=request.data['password']
		user = authenticate(request,username=username, password=password)
		# user=User.objects.filter(username=username).first()
		if user is not None:
			login(request, user)
			token, created = Token.objects.get_or_create(user=user)
			return Response({
				'user_info':{
	            'token': token.key,
	            'user_id': user.pk,
	            'email': user.email,
	            'First_Name':user.first_name,
	            'is_admin':user.is_staff ,
	            },
	            'massage':'Login'
	        })
		if user is None:
			raise AuthenticationFailed("User not found")
		if not user.check_password(password):
			raise AuthenticationFailed("Incorrect password!")
		
class LogOut(APIView):
	def get(self, request, format=None):
		request.user.auth_token.delete()
		return Response({"User Logout"})

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'First_Name':user.first_name,
            'is_admin':user.is_staff ,
        })

class UserDetails(APIView):
	def get(self,request,format=None):
		user=request.user
		if user.is_authenticated:
			return Response({
            'user_id': user.pk,
            'User Name': user.username,
            'email': user.email,
            'First_Name':user.first_name,
            'is_admin':user.is_staff ,
        })
		return Response({"Error"})



