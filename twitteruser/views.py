from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet

@login_required
def home_view(request):
    tweets = Tweet.objects.all().order_by('created_at').reverse()
    return render(request, 'user/homepage.html', {'tweets':tweets})

def profile_view(request, user_id):
    user_obj = TwitterUser.objects.get(id=user_id)
    tweets = Tweet.objects.filter(user=user_obj).order_by('created_at').reverse()
    return render(request, 'user/profile.html', {'user':user_obj, 'tweets':tweets, 'template_name': 'ext/count.html'})

def follow(request):
    follower = TwitterUser.objects.filter(following=request.user).count()
    following = TwitterUser.objects.filter(followers=request.user).count()
    return render(request, 'ext/followers.html', {'follower': follower, 'following':following})

# def follow(request):
#     my_obj = TwitterUser.objects.all()
#     return render(request, 'followers.html', {'my_obj':my_obj})

# def unfollow(request, target_id):
#     follow = TwitterUser.objects.filter(user=request.user, target_id=target_id).first()
#     if follow is not None:
#         follow.delete()
#     return redirect('profile_view')

