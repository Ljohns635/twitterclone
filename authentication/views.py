from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import TwitterUser
from authentication.forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('twitteruser:home_view')))

    form = LoginForm()
    return render(request, 'forms/generic.html', {'form': form, 'heading_one': 'Login'})

def signup_view(request):
    context = {}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            TwitterUser.objects.create_user(
                first_name = data['first_name'],
                last_name = data['last_name'],
                username = data['username'],
                email = data['email'],
                password = data['password'],
            )
            return HttpResponseRedirect(reverse('twitteruser:home_view'))
    form = SignUpForm()
    context.update({'form': form, 'heading_two': 'Sign Up'})
    return render(request, 'forms/generic.html', context)

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
