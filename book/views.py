from rest_framework import generics, filters
from .serializers import BookSerializer, BookOrderSerializer, BookOrderCreateSerializer
from .models import Book, BookOrder
from utils.paginations import StandardResultsSetPagination

class ListBooksView(generics.ListAPIView):
    queryset = Book.objects.all().filter(is_active=True).order_by("created")
    serializer_class = BookSerializer
    search_fields = ['title', 'author', 'translator']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ['id', 'created']
    pagination_class = StandardResultsSetPagination

class BookOrderListView(generics.ListAPIView):
    queryset = BookOrder.objects.all()
    serializer_class = BookOrderSerializer
    pagination_class = StandardResultsSetPagination

class BookOrderCreateView(generics.CreateAPIView):
    queryset = BookOrder.objects.all()
    serializer_class = BookOrderCreateSerializer
