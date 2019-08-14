from django.urls import path
from .views import ListBooksView, BookOrderListView, BookOrderCreateView
from .function_views import *

urlpatterns = [
    path(r'all/', ListBooksView.as_view(), name="books-all"),
    path(r'order/', BookOrderListView.as_view(), name="orders"),
    path(r'order/new', BookOrderCreateView.as_view(), name="new-order"),
]
