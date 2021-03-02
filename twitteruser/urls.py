from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('profile/<int:user_id>/', views.profile_view, name='profile_view'),
]