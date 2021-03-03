from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_tweet, name='create_tweet'),
    path('tweet/<int:tweet_id>/', views.tweet_details, name='tweet_details'),
    # path('count/', views.tweet_count, name='tweet_count'),
]
