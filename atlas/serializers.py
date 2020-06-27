from rest_framework import serializers
from .models import Atlas, AtlasCategory

class AtlasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atlas
        fields = ("name", "body", "category", "image_url", "video_url")

class AtlasCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AtlasCategory
        fields = ('name', 'id', 'image_url')

class AtlasAndCategorySerializer(serializers.ModelSerializer):
    salam = serializers.SerializerMethodField()

    class Meta:
        model = Atlas
        fields = ("name", "body", "category", "image_url")
