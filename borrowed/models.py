# borrowed/models.py
from django.db import models
from books.models import Book
from django.contrib.auth.models import User

class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed_books_in_borrowed')
    borrowed_at = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()

    def __str__(self):
        return f"{self.book.title} borrowed by {self.user.username}"
