from django.urls import path
from .views import ListBooksView

urlpatterns = [
    path(r'all/', ListBooksView.as_view(), name="books-all"),
]