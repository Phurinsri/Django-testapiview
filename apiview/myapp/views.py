from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *


# Create your views here.
def home(request):
    allbooks = Book.objects.all()
    return render(request, 'home.html', {
        # <QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]>
        "allbooks":allbooks,
        # <QuerySet [{'id': 1, 'title': 'Learn apiview', 'author': 'Boss'}, {'id': 2, 'title': 'Learn apiview2', 'author': 'Boss2'}]>
        "allbooksvalues":allbooks.values(),
    })

class BookApiView(APIView):

    @staticmethod
    def get(request, *arg, **kwarg):
        allbooks = Book.objects.all().values()
        return Response(
            {
            "Message": "List of Books",
            "Book list": allbooks,
            }
        )
    
    
    def post(self, request, *arg, **kwarg):
        Book.objects.create(
            id = request.data.get('id'),
            title = request.data.get('title'),
            author = request.data.get('author'),
        )
        book = Book.objects.filter(id= request.data.get('id')).values()
        return Response(
            {
            "Message": "New Book Added!",
            "Book ": book,
            }
        )
