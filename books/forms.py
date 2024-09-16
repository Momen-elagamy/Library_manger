from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'description', 'available', 'image']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'available': forms.CheckboxInput(),  # Ensures it's rendered as a checkbox
        }



class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = []  # Since the BorrowBookForm is not meant to have any fields

    def save(self, commit=True):
        book = super().save(commit=False)
        if commit:
            book.save()
        return book
