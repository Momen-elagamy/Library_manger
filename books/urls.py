from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),               # List all books
    path('add/', views.add_book, name='add_book'),     # Add a new book
    path('<int:id>/borrow/', views.borrow_book, name='borrow_book'),  # Borrow a specific book
    path('<int:id>/edit/', views.book_edit, name='book_edit'),        # Edit a specific book
    path('<int:id>/delete/', views.book_delete, name='book_delete'),  # Delete a specific book
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]