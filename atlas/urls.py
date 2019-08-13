from django.urls import path
from .views import AtlasListView

urlpatterns = [
    path('<int:cat_id>', AtlasListView.as_view(), name="atlas-cat"),
]
