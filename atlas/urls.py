from django.urls import path
from .views import AtlasListView, AtlasAndCategoriesListView, AtlasSearchView
from .function_views import AtlasCategoryListView

urlpatterns = [
    path('all/', AtlasSearchView.as_view(), name="atlas-search"),
    path('<int:cat_id>', AtlasListView.as_view(), name="atlas-cat"),
    path('with-category/<int:cat_id>', AtlasCategoryListView, name="atlas-cat"),
]