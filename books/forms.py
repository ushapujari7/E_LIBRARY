from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date','isbn', 'available_copies']
        widgets = {
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            # 'capable_subjects': forms.CheckboxSelectMultiple(),
         # 'salary': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),  # Prevents negative numbers
        }