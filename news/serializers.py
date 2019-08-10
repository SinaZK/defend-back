from rest_framework import serializers

from .models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("title", "body", "date", "time", "image_url", "video_utl")