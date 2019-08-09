from rest_framework import generics, filters
from .serializers import BookSerializer
from .models import Book
from utils.paginations import StandardResultsSetPagination

class ListBooksView(generics.ListAPIView):
    queryset = Book.objects.all().order_by("created")
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'created']
    pagination_class = StandardResultsSetPagination
