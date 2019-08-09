from django.urls import path
from .views import UserListView

urlpatterns = [
    path(r'', UserListView.as_view()),
]