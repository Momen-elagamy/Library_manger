from django.urls import path
from .views import profile, change_password

urlpatterns = [
    path('', profile, name='profile'),
    path('my_profile/change-password/', change_password, name='change_password'),
    # Other URL patterns
]
