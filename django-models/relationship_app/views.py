from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    book_list = "\n".join([f"Title: {book.title}, Author: {book.author.name}" for book in books])
    return HttpResponse(book_list, content_type="text/plain")
