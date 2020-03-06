from django.urls import path
from .function_views import *

urlpatterns = [
    path(r'sync/', sync, name="sync"),
    path(r'search/', search_all, name="search"),
]