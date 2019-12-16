from rest_framework import serializers
from .models import Infographic, InfographicCategory

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infographic
        fields = ("name", "body", "category", "image_url")

class InfoCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InfographicCategory
        fields = ('name', 'id')

class InfoAndCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Infographic
        fields = ("name", "body", "category", "image_url")
