from django.urls import path
from .views import UserListView
from .function_views import *

urlpatterns = [
    path(r'', UserListView.as_view()),
    path(r'login/', login, name='login'),
]