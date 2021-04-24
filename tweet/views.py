from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet.forms import TweetForm
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from notification.models import Notification
import re

@login_required
def create_tweet(request):
    context = {}
    notify = Notification.objects.filter(reciever=request.user, read=False).count()
    form = TweetForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        new_data = Tweet.objects.create(
                user = request.user,
                body = data['body']
            )
        # __author__ = "Recieved help from my facilitator Elizabeth"
        notifications = re.findall(r'@(\S+)', data['body'])
        for string in notifications:
            user = TwitterUser.objects.filter(username=string).first()
            if user:
                Notification.objects.create(
                    read = False,
                    content_type = new_data,
                    reciever = user
                )
        print(notifications)
        return HttpResponseRedirect(reverse('tweet:tweet_details', args=[new_data.id]))
    
    form = TweetForm()
    context.update({'form': form, 'heading_three': 'Tell everybody what you\'re up to! What\'s new? What\'s changed?', 'notify':notify})
    return render(request, 'forms/generic.html', context)

def tweet_details(request, tweet_id):
    notify = Notification.objects.filter(reciever=request.user, read=False).count()
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, 'tweet_detail.html', {'tweet':tweet, 'notify':notify})


