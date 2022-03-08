from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.

def list_books(request):
    book = Book.objects.all()
    return render(request, "books/list_books.html",{"book": book})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm()
    return render (request, "books/book_detail.html", {"book": book, "pk":pk, "form": form},)

def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="list_books")
    return render(request, "books/add_book.html", {form: form})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
    else:
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(to="list_books")
    return render(request, "books/edit_book.html", {"form": form, "book": book})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect(to="list_books")
    return render(request, "books/delete_book.html", {"book": book})