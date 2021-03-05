from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet

@login_required
def home_view(request):
    user = request.user
    twitteruser = user.following.all()
    tweets = Tweet.objects.filter(user__in=[n for n in twitteruser]).order_by('created_at').reverse()
    # tweets = Tweet.objects.filter(user=twitteruser[0])
    # tweets = Tweet.objects.all().order_by('created_at').reverse()
    return render(request, 'user/homepage.html', {'tweets':tweets})

def profile_view(request, user_id):
    user_obj = TwitterUser.objects.get(id=user_id)
    tweets = Tweet.objects.filter(user=user_obj).order_by('created_at').reverse()
    following = user_obj.following.all().count()
    follower = user_obj.followers.all().count()
    return render(request, 'user/profile.html', {
        'user':user_obj,
        'tweets':tweets,
        # 't_count': t_count,
        'follower': follower,
        'following':following
        })

# def follow_count(request):
#     follower = TwitterUser.objects.filter(following=request.user).count()
#     following = TwitterUser.objects.filter(followers=request.user).count()
#     return render(request, 'ext/followers.html', {'follower': follower, 'following':following})

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

