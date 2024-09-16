from django.shortcuts import render
from django.contrib.auth.models import User

def all_users(request):
    users = User.objects.all()
    return render(request, 'all users/all_users.html', {'users': users})