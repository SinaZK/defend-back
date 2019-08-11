from khayyam import JalaliDate

from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework_swagger import renderers
from django.http.response import JsonResponse

from .models import Event

@api_view(['POST', ])
@permission_classes((permissions.IsAuthenticated,))
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer, renderers.JSONRenderer])
def list_event_by_date(request):
    data = request.data
    if not (data.contains('month') or data.contains('year')):
        return JsonResponse(status=400, data={'message': 'bad request'})
    
    j_month = data['month']
    j_year = data['year']

    start_date = JalaliDate(j_year, j_month, 1)
    end_date = JalaliDate(j_year, j_month, 31)

    events = [e in Event.objects.filter(date__lt=end_date, date__gt=start_date)]
    return JsonResponse(status=200, data={'results': events})
