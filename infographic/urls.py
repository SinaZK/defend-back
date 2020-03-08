from django.urls import path
from .views import InfoListView, InfoAndCategoriesListView, InfoSearchView

urlpatterns = [
    path('all/', InfoSearchView.as_view(), name="info-search"),
    path('<int:cat_id>', InfoListView.as_view(), name="info-cat"),
    path('with-category/<int:cat_id>', InfoAndCategoriesListView.as_view(), name="info-and-cat"),
]
