from django.shortcuts import render
from rest_framework import generics, filters, permissions

from .models import News
from .serializers import NewsSerializer
from utils.paginations import StandardResultsSetPagination

class NewsListView(generics.ListAPIView):
    queryset = News.objects.all().filter(is_show=True).order_by("-created")
    permission_classes = ((permissions.IsAuthenticated), )
    serializer_class = NewsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'created']
    pagination_class = StandardResultsSetPagination
