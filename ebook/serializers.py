from rest_framework import serializers
from rest_framework.response import Response
from .models import EBook, EBookOrder

class EBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = EBook
        fields = ("id", "title", "author", "description", "price", "image_url", "file_url")
        read_only_fields = ("id", )

    def __init__(self, instance=None, data={}, **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        user = self.context["request"].user
        if not instance.has_purchased(user):
            ret.pop("file_url")
        return ret

class EBookSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = EBook
        fields = ("id", "title", "author", "image_url")
        read_only_fields = ("id", )

