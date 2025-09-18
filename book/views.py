from django.shortcuts import render
from rest_framework import status
from .serializers import BookSerializers
from .models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET','POST'])
def booklist(request):
    if request.method=='GET':
        books=Book.objects.all()
        serializers=BookSerializers(books,many=True)
        return Response(serializers.data)
    elif request.method=='POST':
        serializers=BookSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def bookdetails(request,pk):
    if request.method=='GET':
        book=Book.objects.get(pk=pk)
        serializers=BookSerializers(book)
        return Response(serializers.data)
    if request.method=='PUT':
        #book=Book.objects.get(pk=pk)
        serializers=BookSerializers(book,data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        