from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name="home"),
    path('profile/',views.profile,name="profile"),
    path('user/<username>/',views.seeUserProfile,name="viewprofile"),
    path('follow/<username>/',views.follow,name="follow"),
    path('unfollow/<username>/',views.unfollow,name='unfollow'),
    path('liked/<pk>/',views.liked,name="liked"),
    path('unliked/<pk>/',views.Unilked,name="unliked"),
]
