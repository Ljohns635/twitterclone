from django.shortcuts import render
from notification.models import Notification
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required

@login_required
def notification_vew(request):
    user = request.user
    notify = Notification.objects.filter(sender = user)
    return render(request, 'notify.html', {'notify': 'This is the notfication page'})
