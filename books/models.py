from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    borrower = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='borrowed_books_in_books')


    def __str__(self):
        return self.title

