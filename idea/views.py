from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response

from utils.paginations import *
from .models import Idea
from .serializers import IdeaSerializer

class UserIdeaCreateView(generics.CreateAPIView):
    serializer_class = IdeaSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Idea.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserIdeaListView(generics.ListAPIView):
    serializer_class = IdeaSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Idea.objects.all()

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset().filter(user=request.user)
        serializer = IdeaSerializer(queryset, many=True)
        return Response(serializer.data)
