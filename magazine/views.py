from rest_framework import generics, filters
from .serializers import MagazineSerializer, MagazineCategorySerializer
from .models import Magazine, MagazineCategory
from utils.paginations import StandardResultsSetPagination
from rest_framework.response import Response

class ListMagazinesView(generics.ListAPIView):
    serializer_class = MagazineSerializer
    search_fields = ['title', 'author']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ['id', 'created']
    pagination_class = StandardResultsSetPagination

    def get_serializer_context(self):
        return {'request': self.request}

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
    
    def get_queryset(self):
        queryset = Magazine.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category__id=category)
        year = self.request.query_params.get('year', None)
        if year is not None:
            queryset = queryset.filter(year=year)
        return queryset

class ListMagazinesCategoryView(generics.ListAPIView):
    queryset = MagazineCategory.objects.all().order_by("created")
    serializer_class = MagazineCategorySerializer
    search_fields = ['title']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ['id', 'created']
    pagination_class = StandardResultsSetPagination