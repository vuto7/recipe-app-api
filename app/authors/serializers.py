import logging

from rest_framework import serializers

from core.models import (Author, Book)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only = True, many = True)
    
    class Meta:
        model = Author
        fields = '__all__'
