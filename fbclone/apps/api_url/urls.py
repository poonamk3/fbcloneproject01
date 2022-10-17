from django.urls import path,include
from api_view.api_views import registreviewapis,LoginApi,LogOut,CustomAuthToken,UserDetails,PostApi,UserList,Mypost
from api_view.api_views import registreviewapi
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.authtoken import views


router = DefaultRouter()
router.register('registerallapi',registreviewapi,basename='Student'),
router.register('post',PostApi,basename='postapi'),
router.register('mypost',Mypost,basename='myapi'),


urlpatterns = [
    path('registerapi/',registreviewapis.as_view(), name='resapi'),
    path('userlist/',UserList.as_view(), name='userlist'),
    path('loginapi/',LoginApi.as_view(), name='loginapi'),
    path('userinfo/',UserDetails.as_view(), name='user-info'),
    path('logoutapi/',LogOut.as_view(), name='loginapi'),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    # path('login/',views.obtain_auth_token,name='api-token-auth'),
    path('login-auth/',CustomAuthToken.as_view()),

]
