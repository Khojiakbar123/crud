from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from book_api.models import Book
from book_api.serializers import BookSerializer


# Create your views here.

# def book_list(request):
#     books = Book.objects.all()
#     return JsonResponse({"books":list(books.values())})

def book_detail(request,pk):
    book = Book.objects.get(pk=pk)
    data = {
        "id":book.pk,
        "title":book.title,
        "author":book.author,
        "price":book.price
    }
    return JsonResponse(data)

@api_view(['GET','POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)