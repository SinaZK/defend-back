from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework_swagger import renderers
from django.http.response import JsonResponse

from users.models import Member
from news.models import News
from news.serializers import NewsSerializer

@api_view(['POST', ])
@permission_classes((permissions.IsAuthenticated,))
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer, renderers.JSONRenderer])
def sync(request):
    data = request.data
    user = request.user
    
    new = News.objects.all().filter(is_show=True).order_by("-created")[0]
    return JsonResponse(data={
        'news': NewsSerializer(new).data,
    })
