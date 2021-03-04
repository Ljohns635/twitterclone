from django.db import models
from django.contrib.auth.models import AbstractUser

class TwitterUser(AbstractUser):
    followers = models.ManyToManyField('self', related_name='user_followers', symmetrical=False, blank=True)
    following = models.ManyToManyField('self', related_name='user_following', symmetrical=False, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', null=True, blank=True)
    background_img = models.ImageField(upload_to='background_img', null=True, blank=True)
    profile_bio = models.CharField(max_length=60)
    location = models.CharField(max_length=50)
    web_url = models.URLField(max_length=100)

    def __str__(self):
        return '@' + self.username
    
