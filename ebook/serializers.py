from rest_framework import serializers
from rest_framework.response import Response
from .models import EBook, EBookOrder

class EBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = EBook
        fields = ("id", "title", "author", "description", "price", "image_url", "file_url")
        read_only_fields = ("id", )
