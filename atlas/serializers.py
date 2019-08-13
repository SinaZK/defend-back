from rest_framework import serializers
from .models import Atlas

class AtlasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atlas
        fields = ("name", "category")
