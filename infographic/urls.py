from django.urls import path
from .views import InfoListView, InfoAndCategoriesListView

urlpatterns = [
    path('<int:cat_id>', InfoListView.as_view(), name="info-cat"),
    path('with-category/<int:cat_id>', InfoAndCategoriesListView.as_view(), name="info-and-cat"),
]
