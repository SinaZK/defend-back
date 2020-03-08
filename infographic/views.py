from django.shortcuts import render
from rest_framework import generics, views, filters
from rest_framework.response import Response

from utils.paginations import *
from .serializers import InfoSerializer, InfoAndCategorySerializer, InfoCategorySerializer
from .models import Infographic, InfographicCategory

class InfoListView(generics.ListAPIView):
    serializer_class = InfoSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        cat_id = self.kwargs['cat_id']
        descendant_cats = InfographicCategory.objects.filter(id=cat_id).get_descendants(include_self=True)
        return Infographic.objects.filter(category__in=descendant_cats)

class InfoAndCategoriesListView(views.APIView, StandardResultsSetPagination):

    def get_queryset(self):
        return Infographic.objects.all()

    def get(self, request, format=None, **kwargs):
        cat_id = self.kwargs['cat_id']
        descendant_cats = InfographicCategory.objects.filter(id=cat_id).get_descendants(include_self=True)
        if descendant_cats.count() == 0:
            descendant_cats = InfographicCategory.objects.filter(parent=None)
            categories = InfoCategorySerializer(descendant_cats, many=True)
        else:
            categories = InfoCategorySerializer(InfographicCategory.objects.get(id=cat_id).get_children(), many=True)
        info = InfoSerializer(self.paginate_queryset(Infographic.objects.filter(category__in=descendant_cats), request=request), many=True)

        return self.get_paginated_response({
            'info': info.data,
            'categories': categories.data,
        })

class InfoSearchView(generics.ListAPIView):
    queryset = Infographic.objects.all().order_by("created")
    serializer_class = InfoSerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ['id', 'created']
    pagination_class = StandardResultsSetPagination
