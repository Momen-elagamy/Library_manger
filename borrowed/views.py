from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import BorrowedBook


@login_required
def borrowed_books(request):
    """View to show borrowed books for both regular users and admin users."""
    if request.user.is_staff:
        # Admin users see all borrowed books
        borrowed_books = BorrowedBook.objects.all()
    else:
        # Regular users see only their own borrowed books
        borrowed_books = BorrowedBook.objects.filter(user=request.user)

    return render(request, 'borrowed/my_borrowed_books.html', {'borrowed_books': borrowed_books})


@login_required
def my_borrowed_books(request):
    """View to show only the borrowed books of the logged-in user."""
    print(request.user)  # Debugging: Should print the logged-in user

    borrowed_books = BorrowedBook.objects.filter(user=request.user)
    print(borrowed_books)  # Debugging: Check if the queryset returns anything

    if borrowed_books.exists():
        return render(request, 'borrowed/my_borrowed_books.html', {'borrowed_books': borrowed_books})
    else:
        return render(request, 'borrowed/no_borrowed_books.html')  # Message if no books are borrowed


@login_required
def all_borrowed_books(request):
    """Admin view to show all borrowed books."""
    if request.user.is_staff:  # Only for admin users
        borrowed_books = BorrowedBook.objects.all()
        return render(request, 'borrowed/all_borrowed_books.html', {'borrowed_books': borrowed_books})
    else:
        return render(request, 'borrowed/not_authorized.html')  # Message for unauthorized access
