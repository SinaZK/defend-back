from rest_framework import generics, filters
from .serializers import EBookSerializer
from .models import EBook
from utils.paginations import StandardResultsSetPagination
from rest_framework.response import Response

class ListEBooksView(generics.ListAPIView):
    queryset = EBook.objects.all().filter(is_active=True).order_by("created")
    serializer_class = EBookSerializer
    filter_backends = [filters.OrderingFilter]
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
