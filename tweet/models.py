from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser

class Tweet(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, null=True)
    liked = models.ManyToManyField(TwitterUser, related_name='liked_tweet')