from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models


def index(request):
    return HttpResponse("Hello, world.")


def all_books(request):
    books = models.Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'all_books.html', {'context': context})


def book_detail(request, book_id):
    book = get_object_or_404(models.Book, id=book_id)
    context = {
        'book': book,
    }
    return render(request, 'book.html', {'context': context})


def book_review(request, book_id):
    book = get_object_or_404(models.Book, id=book_id)
    reviews = models.Review.objects.filter(book=book_id)
    context = {

        'book': book,
        'reviews': reviews,

    }
    return render(request, 'review.html', {'context': context})
