from django.urls import path
from . import views

app_name = 'notification'

urlpatterns = [
    path('notifications/', views.notification_vew, name='notification_view'),
]