# borrowed/admin.py
from django.contrib import admin
from .models import BorrowedBook



@admin.register(BorrowedBook)
class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'borrowed_at', 'return_date')

