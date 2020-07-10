from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework_jwt.settings import api_settings
from rest_framework_swagger import renderers
from django.http.response import JsonResponse
from .models import AtlasCategory, Atlas
from .serializers import AtlasCategorySerializer, AtlasSerializer

@api_view(['GET', 'POST'])
@permission_classes(())
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer, renderers.JSONRenderer])
def AtlasCategoryListView(request, cat_id):
    descendant_cats = AtlasCategory.objects.filter(id=cat_id).get_descendants(include_self=True)
    last_cat = False
    if descendant_cats.count() == 0:
        descendant_cats = AtlasCategory.objects.filter(parent=None)
        categories = AtlasCategorySerializer(descendant_cats, many=True)
    else:
        count = AtlasCategory.objects.get(id=cat_id).get_children().count()
        if count == 0:
            last_cat = True
        categories = AtlasCategorySerializer(AtlasCategory.objects.get(id=cat_id).get_children(), many=True)
    
    if last_cat:
        atlases = AtlasSerializer(Atlas.objects.filter(category__id=cat_id), many=True)
        return JsonResponse(status=200, data={
         'categories': categories.data,
         'atlases': atlases.data
    })

    return JsonResponse(status=200, data={
         'categories': categories.data
    })