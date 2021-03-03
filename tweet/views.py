from django.shortcuts import render, HttpResponseRedirect, reverse
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
                user = request.user,
                body = data['body']
            )
        return HttpResponseRedirect(reverse('tweet_details', args=[new_data.id]))
    
    form = TweetForm()
    context.update({'form': form, 'heading_three': 'Tell everybody what you\'re up to! What\'s new? What\'s changed?'})
    return render(request, 'forms/generic.html', context)

def tweet_details(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, 'tweet_detail.html', {'tweet':tweet})

def tweet_count(request):
    t_count = Tweet.objects.filter(user=request.user).count()
    return render(request, 'ext/count.html', {'t_count': t_count})

