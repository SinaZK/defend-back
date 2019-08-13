from rest_framework import serializers
from .models import Atlas, AtlasCategory

class AtlasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atlas
        fields = ("name", "body", "category", "image_url")

class AtlasCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AtlasCategory
        fields = ('name', 'id')

class AtlasAndCategorySerializer(serializers.ModelSerializer):
    #next_categories = serializers.ListField(child=AtlasCategorySerializer())
    salam = serializers.SerializerMethodField()

    class Meta:
        model = Atlas
        fields = ("name", "body", "category", "image_url", "salam")

    def get_salam(self, obj):
        return "salam "
