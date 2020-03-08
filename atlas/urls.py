from django.urls import path
from .views import AtlasListView, AtlasAndCategoriesListView, AtlasSearchView

urlpatterns = [
    path('all/', AtlasSearchView.as_view(), name="atlas-search"),
    path('<int:cat_id>', AtlasListView.as_view(), name="atlas-cat"),
    path('with-category/<int:cat_id>', AtlasAndCategoriesListView.as_view(), name="atlas-and-cat"),
]