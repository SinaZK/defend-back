from django.urls import path
from .function_views import list_event_by_date
from .function_views import *

urlpatterns = [
    path(r'', list_event_by_date, name="events-by-month"),
]
