from django.shortcuts import render
from notification.models import Notification
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required

# __author__ = "Recieved help from my facilitator Elizabeth"

@login_required
def notification_vew(request):
    user = request.user
    notifications = Notification.objects.filter(reciever=user, read=False)
    for alert in notifications:
        alert.read = True
        alert.save()
    return render(request, 'notify.html', {'notifications': notifications})
