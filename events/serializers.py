from rest_framework import serializers

from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class meta:
        model = Event
        fields = ('title', 'body', 'jalali_date', 'time', 'image_url', 'location')
