from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect("list_books")
    return render(request, "books/home.html")

def book_is_favorited(book, user):
    return user.favorite_books.filter(pk=book)

@login_required
def list_books(request):
    book = Book.objects.all()
    favorited = book_is_favorited(book, request.user)
    return render(request, "books/list_books.html",{"book": book, "favorited": favorited})
    
@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)  
    form = BookForm()
    return render (request, "books/book_detail.html", {"book": book, "pk":pk, "form": form},)

@login_required
def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="list_books")
    return render(request, "books/add_book.html", {"form": form})

@login_required
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

@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect(to="list_books")
    return render(request, "books/delete_book.html", {"book": book})

@login_required
def sort_by_category(request, slug):
    book = Book.objects.filter(categories__slug=slug)
    return render(request, "books/list_books.html", {"book": book})

@login_required
def add_favorite(request, book):
    book = get_object_or_404(Book, pk=book.pk)
    user = request.user
    user.favorite_books.add(book)
    favorited = book_is_favorited(book, request.user)
    return redirect("list_books", pk = book.pk)
