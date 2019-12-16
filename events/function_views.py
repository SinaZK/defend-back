from khayyam import JalaliDate

from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework_swagger import renderers
from django.http.response import JsonResponse

from .models import Event
from .serializers import EventSerializer

@api_view(['POST', ])
@permission_classes((permissions.IsAuthenticated,))
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer, renderers.JSONRenderer])
def list_event_by_date(request):
    data = request.data
    if not ('month' in data or 'year' in data):
        return JsonResponse(status=400, data={'message': 'bad request'})
    
    j_month = data['month']
    j_year = data['year']

    start_date = JalaliDate(j_year, j_month, 1)
    end_date = JalaliDate(j_year, j_month, start_date.daysinmonth)

    events = [] 
    for e in Event.objects.filter(date__lte=end_date.todate(), date__gte=start_date.todate()):
        if e.user_event and not e.admin_approved:
            continue
        events.append(EventSerializer(e).data)
    return JsonResponse(status=200, data={'results': events})
