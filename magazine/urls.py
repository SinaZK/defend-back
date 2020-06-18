from django.urls import path
from .views import ListMagazinesView

urlpatterns = [
    path(r'all/', ListMagazinesView.as_view(), name="magazines-all"),
]
