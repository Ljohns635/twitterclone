from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import TwitterUser
from authentication.forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    form = LoginForm()
    return render(request, 'generic.html', {'form': form})

def signup_view(request):
    form = SignUpForm()
    return render(request, 'generic.html', {'form': form})
