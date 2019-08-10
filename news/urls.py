from django.urls import path
from .views import NewsListView

urlpatterns = [
    path(r'', NewsListView.as_view(), name="news-all"),
]