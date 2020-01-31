from rest_framework import serializers

from .models import Idea

class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ('title', 'body', 'name', 'service_location', 'education_degree',
        'education_field', 'phone_number', 'internet_address', 'physical_address', 'category',
        'state', 'state_text', 'code', 'state_fa')
        read_only_fields = ('state', 'state_text', 'code')

