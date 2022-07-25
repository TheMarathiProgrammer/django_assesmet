from urllib import response
from django.shortcuts import render
from .models import Books
from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import BookDetails, CreatBook,UserSerializer,UserLoginSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here.
class BooksListView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookDetails
    permission_classes = (IsAuthenticated,)

class CreateBooks(generics.GenericAPIView):
    queryset = Books.objects.all()
    serializer_class = CreatBook
    permission_classes = (IsAuthenticated,IsAdminUser)
    def post(self,request,*args,**kwargs):
        self.request = request 
        self.serializer = self.get_serializer(data=request.data)
        if Books.objects.filter(isbn = request.data['isbn']).exists():
            return Response(status=status.HTTP_409_CONFLICT,data='ISBN No. is already exists')
        else:
            self.serializer.is_valid(raise_exception=True)
            resp = self.serializer.save()
            return Response(status=status.HTTP_200_OK)

class UpdateBook(generics.GenericAPIView):
    serializer_class = BookDetails 
    permission_classes = (IsAuthenticated,IsAdminUser)
    def put(self,request,*args,**kwargs):
        self.request = request
        book_data = Books.objects.get(id = self.kwargs['id'])
        data = BookDetails(instance=book_data,data=request.data)
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_200_OK,data=data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeleteBook(generics.GenericAPIView):
    serializer_class = BookDetails
    permission_classes = (IsAuthenticated,IsAdminUser)
    def delete(self,request,*args,**kwargs):
        self.request = request
        book_data = Books.objects.get(id = self.kwargs['id'])
        if book_data:
            book_data.delete()
            return Response(status=status.HTTP_200_OK,data="Data Has Been Deleted!!!")
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class RegisterUser(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def post(self,request,*args,**kwargs):
        self.request = request 
        self.serializer = self.get_serializer(data=request.data)
        self.serializer.is_valid(raise_exception=True)
        resp = self.serializer.save()
        return Response(status=status.HTTP_200_OK)

class LoginUser(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.get(username=username,password=password)
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED,data='Invalid Credentials')
        else:
            token = Token.objects.get_or_create(user=user)
            return Response({'token':token[0].key},status=status.HTTP_200_OK)