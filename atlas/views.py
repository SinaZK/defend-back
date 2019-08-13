from django.shortcuts import render
from rest_framework import generics

from utils.paginations import *
from .serializers import AtlasSerializer
from .models import Atlas, AtlasCategory

class AtlasListView(generics.ListAPIView):
    serializer_class = AtlasSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        cat_id = self.kwargs['cat_id']
        descendant_cats = AtlasCategory.objects.filter().get_descendants(include_self=True)
        return Atlas.objects.filter(category__in=descendant_cats)
