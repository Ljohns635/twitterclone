from django.urls import path
from . import views

app_name = 'twitteruser'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('profile/<int:user_id>/', views.profile_view, name='profile_view'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
]