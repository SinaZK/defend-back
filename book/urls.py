from django.urls import path
from .views import ListBooksView
from .function_views import *

urlpatterns = [
    path(r'all/', ListBooksView.as_view(), name="books-all"),
    path(r'test/', test, name="test-all"),
]