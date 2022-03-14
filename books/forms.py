from django import forms
from .models import Book, Topic

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'description',
            'url',
            'topic',
            'created_at',
            
        ]