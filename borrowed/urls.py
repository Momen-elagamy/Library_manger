# borrowed/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('borrowed/', views.borrowed_books, name='borrowed_books'),
    path('my-borrowed-books/', views.my_borrowed_books, name='my_borrowed_books'),
    path('all-borrowed-books/', views.all_borrowed_books, name='all_borrowed_books'),
]
