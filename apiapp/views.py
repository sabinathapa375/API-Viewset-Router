from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import BookSerializer
from .models import Book

# Create your views here.
class BookViewSet(viewsets.ViewSet):
    
    #To display all the list
    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    #To retrive only one data
    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            books = Book.objects.get(id=id)
            serializer = BookSerializer(books)
            return Response(serializer.data)
        
    #to create the data
    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    #To update data
    def update(self, request, pk):
        id = pk
        books = Book.objects.get(pk=id)
        serializer = BookSerializer(books, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Update completed.'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    #For partial update
    def partial_update(self, request,pk):
        id = pk
        books = Book.objects.get(pk=id)
        serializer = BookSerializer(books, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial update completed.'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    #For deletion
    def destroy(self, request,pk):
        id = pk
        books = Book.objects.get(pk=id)
        books.delete()
        return Response({'msg':'Data Deleted'})
    
        
    