from django.urls import path
from .views import ListEBooksView

urlpatterns = [
    path(r'all/', ListEBooksView.as_view(), name="ebooks-all"),
]
