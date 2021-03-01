from django.urls import path
from authentication.views import signup_view, login_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
]
