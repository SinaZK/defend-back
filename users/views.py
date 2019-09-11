from rest_framework import generics

from . import models
from . import serializers

class UserListView(generics.CreateAPIView):
    permission_classes = ()
    queryset = models.Member.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = ()
