from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('home/',views.IndexView.as_view(),name="homes"),
    path('', views.PostListView.as_view(),name="home"),
    path('postsuccess/', views.PostSuccessView.as_view()),
    path('register/', views.RegisterView.as_view(),name="register"),
    path('accounts/profile/',views.ProfileView.as_view(),name="profile"),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='enroll/logout.html'), name='logout'),
    path('post/', views.PostView.as_view(),name="post"),
    # path('post/', views.CommentsView.as_view(),name="post"),
    # path('postlist/', views.PostListView.as_view(),name="postlist"),
    path('mypost/', views.MyPostView.as_view(),name="mypost"),
    path('detail/<int:id>', views.PostDetailView.as_view(),name="mypostdeatils"),
    path('update/<int:pk>', views.UpdateView.as_view(),name="updateview"),   
    path('delete/<int:pk>', views.DeleteView.as_view(),name="deleteview"),
    path('like/', views.like_post,name="like-post"),
    path('comment/', views.add_comment,name="mment"),
    
    
]
