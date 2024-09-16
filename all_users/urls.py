from django.urls import path
from .views import all_users

urlpatterns = [
    path('all_users/', all_users, name='all_users'),
]
