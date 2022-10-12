from django.urls import path,include
from api_view.api_views import registreviewapis,LoginApi,LogOut,CustomAuthToken,UserDetails,PostApi
from api_view.api_views import registreviewapi
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.authtoken import views


router = DefaultRouter()
router.register('registerapi',registreviewapi,basename='Student'),
router.register('post',PostApi,basename='postapi')


urlpatterns = [
    path('register/', registreviewapis.as_view(), name='resapi'),
    path('login', LoginApi.as_view(), name='loginapi'),
    path('userinfo/', UserDetails.as_view(), name='user-info'),
    path('logout/', LogOut.as_view(), name='loginapi'),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    # path('login/',views.obtain_auth_token,name='api-token-auth'),
    path('login-auth/', CustomAuthToken.as_view()),

]
