from django.shortcuts import render
from rest_framework import generics, views, filters
from rest_framework.response import Response

from utils.paginations import *
from .serializers import AtlasSerializer, AtlasAndCategorySerializer, AtlasCategorySerializer
from .models import Atlas, AtlasCategory

class AtlasListView(generics.ListAPIView):
    serializer_class = AtlasSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        cat_id = self.kwargs['cat_id']
        descendant_cats = AtlasCategory.objects.filter(id=cat_id, removed=None).get_descendants(include_self=True)
        return Atlas.objects.filter(category__in=descendant_cats)

class AtlasCategoryListView(views.APIView, StandardResultsSetPagination):

    def get_queryset(self):
        return AtlasCategory.objects.filter(removed=None)

    def get(self, request, format=None, **kwargs):
        cat_id = self.kwargs['cat_id']
        descendant_cats = AtlasCategory.objects.filter(id=cat_id).get_descendants(include_self=True)
        if descendant_cats.count() == 0:
            descendant_cats = AtlasCategory.objects.filter(parent=None)
            categories = AtlasCategorySerializer(descendant_cats, many=True)
        else:
            categories = AtlasCategorySerializer(AtlasCategory.objects.get(id=cat_id).get_children().filter(removed=None), many=True)

        return self.get_paginated_response({
            'categories': categories.data
        })

class AtlasAndCategoriesListView(views.APIView, StandardResultsSetPagination):

    def get_queryset(self):
        return Atlas.objects.filter(removed=None)

    def get(self, request, format=None, **kwargs):
        cat_id = self.kwargs['cat_id']
        descendant_cats = AtlasCategory.objects.filter(id=cat_id).get_descendants(include_self=True)
        if descendant_cats.count() == 0:
            descendant_cats = AtlasCategory.objects.filter(parent=None, removed=None)
            categories = AtlasCategorySerializer(descendant_cats, many=True)
        else:
            categories = AtlasCategorySerializer(AtlasCategory.objects.get(id=cat_id).get_children().filter(removed=None), many=True)
        atlases = AtlasSerializer(self.paginate_queryset(Atlas.objects.filter(category__in=descendant_cats).filter(removed=None), request=request), many=True)

        return self.get_paginated_response({
            'atlases': atlases.data,
            'categories': categories.data,
        })

class AtlasSearchView(generics.ListAPIView):
    queryset = Atlas.objects.all().order_by("created")
    serializer_class = AtlasSerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ['id', 'created']
    pagination_class = StandardResultsSetPagination
