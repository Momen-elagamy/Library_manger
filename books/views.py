from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from borrowed.models import BorrowedBook
from django.utils import timezone
from datetime import timedelta



@login_required(login_url='index')
def borrow_book(request, id):
    """View to borrow a book."""
    book = get_object_or_404(Book, id=id)

    if not book.available:
        messages.error(request, 'This book is currently not available.')
        return redirect('books')

    if request.method == 'POST':
        # Debugging to ensure POST request is working
        print(f"Borrowing book: {book.title} by {request.user.username}")

        # Mark book as borrowed
        book.available = False
        book.borrower = request.user
        book.save()

        # Set return date (e.g., 2 weeks from now)
        return_date = timezone.now() + timedelta(weeks=2)

        # Create an entry in BorrowedBook
        borrowed_book = BorrowedBook.objects.create(
            book=book,
            user=request.user,
            return_date=return_date
        )
        print(f"BorrowedBook created: {borrowed_book}")  # Debugging to confirm record is created

        messages.success(request, 'You have successfully borrowed the book.')
        return redirect('borrowed_books')

    return render(request, 'books/borrow_book.html', {'book': book})


def books(request):
    """View to list all books."""
    books = Book.objects.all()
    return render(request, 'books/books.html', {'books': books})


@login_required
def add_book(request):
    """View to add a new book."""
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully.')
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})


@login_required
def book_edit(request, id):
    """View to edit a book's details."""
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully.')
            return redirect('books')
    else:
        form = BookForm(instance=book)

    return render(request, 'books/book_form.html', {'form': form})


@login_required
def book_delete(request, id):
    """View to delete a book."""
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully.')
        return redirect('books')
    return render(request, 'books/book_confirm_delete.html', {'book': book})


@login_required
def borrowed_books(request):
    """View to list borrowed books."""
    if request.user.is_staff:
        # Admin user can see all borrowed books
        borrowed_books = BorrowedBook.objects.all()
    else:
        # Regular user can see only their borrowed books
        borrowed_books = BorrowedBook.objects.filter(user=request.user)

    return render(request, 'borrowed/borrowed_books.html', {'borrowed_books': borrowed_books})
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})