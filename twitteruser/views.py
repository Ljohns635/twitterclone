from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification.models import Notification

# __author__ = "Recieved help from Martin Villa getting homepage to show not just following users but the following user and current signed in user post"

@login_required
def home_view(request):
    # user = request.user
    # twitteruser = user.following.all()
    # tweets = Tweet.objects.filter(user__in=[n for n in twitteruser]).order_by('created_at').reverse()
    notify = Notification.objects.filter(reciever=request.user, read=False).count()
    tweets = Tweet.objects.all().order_by('created_at').reverse()
    tweets = [n for n in tweets if n.user in request.user.following.all() or request.user == n.user]
    return render(request, 'user/homepage.html', {'tweets':tweets, 'notify':notify})

def profile_view(request, user_id):
    user_obj = TwitterUser.objects.get(id=user_id)
    tweets = Tweet.objects.filter(user=user_obj).order_by('created_at').reverse()
    following = user_obj.following.all().count()
    follower = user_obj.followers.all().count()
    t_count = Tweet.objects.filter(user=user_id).count()
    return render(request, 'user/profile.html', {
        'user':user_obj,
        'tweets':tweets,
        't_count': t_count,
        'follower': follower,
        'following':following
        })

@login_required
def follow_user(request, user_id):
    logged_in_user = request.user
    to_be_followed = TwitterUser.objects.get(id=user_id)
    logged_in_user.following.add(to_be_followed)
    logged_in_user.save()
    return HttpResponseRedirect('/')

@login_required
def unfollow_user(request, user_id):
    logged_in_user = request.user
    to_be_unfollowed = TwitterUser.objects.get(id=user_id)
    logged_in_user.following.remove(to_be_unfollowed)
    logged_in_user.save()
    return HttpResponseRedirect('/')

