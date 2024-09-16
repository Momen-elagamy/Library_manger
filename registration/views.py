from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

def index(request):
    return render(request, 'registration/index.html')  # Ensure this path is correct

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('books')  # Redirect to a success page or homepage
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Automatically log in the user
            messages.success(request, 'Your account has been created successfully.')
            return redirect('login')  # Redirect to the homepage or another page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()

    return render(request, 'registration/registration.html', {'form': form})

# Renaming the logout view to avoid conflict
def logout_view(request):
    # Allow logout on GET request as well
    if request.method == 'POST' or request.method == 'GET':
        auth_logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('login')