from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import TwitterUser
from tweet.forms import TweetForm
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required

@login_required
def create_tweet(request):
    context = {}
    form = TweetForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        new_data = Tweet.objects.create(
                body = data['body']
            )
        return HttpResponseRedirect(reverse('home_view', args=[new_data.id]))
    
    form = TweetForm()
    context.update({'form': form})
    return render(request, 'tweet.html', context)

def tweet_details(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, 'tweet_detail.html', {'tweet':tweet})

