from rest_framework import serializers
from rest_framework.response import Response
from .models import Magazine, MagazineCategory, MagazineOrder

class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = ("id", "title", "author", "description", "price", "image_url", "file_url", "year")
        read_only_fields = ("id", )

    def __init__(self, instance=None, data={}, **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        user = self.context["request"].user
        if not instance.has_purchased(user):
            ret.pop("file_url")
        return ret

class MagazineSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = ("id", "title", "author", "description", "price", "image_url", "file_url")
        read_only_fields = ("id", )

class MagazineCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MagazineCategory
        fields = ("id", "title", "image_url")
        read_only_fields = ("id", )
