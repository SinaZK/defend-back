from rest_framework import serializers
from .models import Member

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Member
        fields = ('id', 'email', 'username', 'password')

    def create(self, validated_data):

        user = Member.objects.create(
            username=validated_data['username'],
            email=validated_data.get('email', '')
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
