from django.db import models
from twitteruser.models import TwitterUser
from tweet.models import Tweet

class Notification(models.Model):
    sender = models.ForeignKey(TwitterUser, related_name='t_sender', on_delete=models.CASCADE)
    reciever = models.ForeignKey(TwitterUser, related_name='t_receiver', on_delete=models.CASCADE)
    update_at = models.DateTimeField(auto_now=True)
    read = models.BooleanField(default=False)
    content_type = models.ForeignKey(Tweet, related_name='notify_tweet', on_delete=models.CASCADE)

def __str__(self):
    return self.content_type
