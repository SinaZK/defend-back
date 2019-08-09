from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework_jwt.settings import api_settings
from rest_framework_swagger import renderers
from django.http.response import JsonResponse

@api_view(['POST', ])
@permission_classes((permissions.IsAuthenticated,))
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer, renderers.JSONRenderer])
def test(request):
    print(request.user, 'id = ', request.user.id)

    return JsonResponse(status=200, data={})