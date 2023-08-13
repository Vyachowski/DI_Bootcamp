from django.shortcuts import render
from models import Book
from django.http import JsonResponse
# Create your views here.


def list_books(request):
    books = Book.objects.all()
    data = [{'id': book.id, 'title': book.title, 'author': book.author} for book in books]
    return JsonResponse(data)



