from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet

@login_required
def home_view(request):
    tweets = Tweet.objects.all().order_by('created_at').reverse()
    return render(request, 'homepage.html', {'header': 'this is a header', 'tweets':tweets})

def profile_view(request, username):
    user_obj = TwitterUser.objects.get(username=username)
    tweets = Tweet.objects.filter(user=user_obj).order_by('created_at').reverse()
    return render(request, 'profile.html', {'user':user_obj, 'tweets':tweets})


