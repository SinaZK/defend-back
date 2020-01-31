from django.urls import path
from .views import *

urlpatterns = [
    path(r'', UserIdeaListView.as_view(), name="ideas-user"),
    path(r'create/', UserIdeaCreateView.as_view(), name="create-user-idea"),
]
