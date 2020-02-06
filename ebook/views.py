from rest_framework import generics, filters
from .serializers import EBookSerializer
from .models import EBook
from utils.paginations import StandardResultsSetPagination

class ListEBooksView(generics.ListAPIView):
    queryset = EBook.objects.all().filter(is_active=True).order_by("created")
    serializer_class = EBookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'created']
    pagination_class = StandardResultsSetPagination
