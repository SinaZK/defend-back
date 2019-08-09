from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework_jwt.settings import api_settings
from rest_framework_swagger import renderers
from django.http.response import JsonResponse

from .models import Member
from .serializers import UserLoginSerializer

@api_view(['POST', ])
@permission_classes(())
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer, renderers.JSONRenderer])
def login(request):
    data = request.data
    
    try:
        member = Member.objects.get(username=data.get('username', ''))
    except Member.DoesNotExist:
        return JsonResponse(status=401, data={})

    if member.check_password(data.get('password', '')):
        return JsonResponse(status=200, data=UserLoginSerializer(member).data)
    else:
        return JsonResponse(status=401, data={})
