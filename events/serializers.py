from rest_framework import serializers

from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'body', 'jalali_date', 'time', 'image_url', 'location', 'date')
