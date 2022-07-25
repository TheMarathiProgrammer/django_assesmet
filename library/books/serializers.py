from dataclasses import field, fields
from rest_framework import serializers
from .models import Books
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class BookDetails(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id','isbn','title','author')

class CreatBook(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('isbn','title','author')

class UserSerializer(serializers.ModelSerializer):
    userqueryset = User.objects.all()
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=userqueryset)]
    )
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name','email')

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')
