from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    message = 'Hello, this is my first page'
    return HttpResponse(message)

def post(request, post_id: int):
    data = {
        1: 'This is the first post',
        2: 'This is the second post',
    }
    post = data.get(post_id, 'No such post')
    return HttpResponse(post)

def about(request):
    return HttpResponse('<h1> Welcome Users<h1>')

def all_posts(request, author_name:str):
    pass
    return HttpResponse('<h1> Welcome Users<h1>')