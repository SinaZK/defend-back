from django.urls import path
from .views import ListMagazinesView, ListMagazinesCategoryView

urlpatterns = [
    path(r'all/', ListMagazinesView.as_view(), name="magazines-all"),
    path(r'categories/', ListMagazinesCategoryView.as_view(), name="magazines-cat-all"),
]
