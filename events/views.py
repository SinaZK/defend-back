from django.shortcuts import render
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework import generics, views
from rest_framework.response import Response

from utils.paginations import *
from .models import Event
from .serializers import EventSerializer

class UserEventCreateView(generics.CreateAPIView):
    serializer_class = EventSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Event.objects.all()
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, user_event=True)
