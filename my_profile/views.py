from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from books.models import Book  # Adjust import based on your app structure

@login_required
def profile(request):
    borrowed_books = Book.objects.filter(borrower=request.user)  # Ensure the field name matches your model
    return render(request, 'my_profile/profile.html', {'borrowed_books': borrowed_books})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'my_profile/change_password.html', {'form': form})
