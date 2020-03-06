from rest_framework import serializers

from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'body', 'jalali_date', 'jalali_end_date', 'time', 'image_url', 'location', 'date', 'image',
            'end_time', 'end_date', 'info')
