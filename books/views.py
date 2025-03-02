from urllib import request

from django.shortcuts import render, redirect
from .forms import BookForm # Import the form
from .models import Book # Import the model

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Save the book to the database
            return redirect('book_list')  # Redirect to book list after adding
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


def book_list(request):
        books = Book.objects.all()  # Retrieve all books from the database
        return render(request, 'book_list.html', {'books': books})