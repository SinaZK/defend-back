from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework_swagger import renderers
from django.http.response import JsonResponse

from users.models import Member
from news.models import News
from news.serializers import NewsSerializer

from atlas.models import Atlas
from atlas.serializers import AtlasSerializer
from book.models import Book
from book.serializers import BookSerializer
from infographic.models import Infographic
from infographic.serializers import InfoSerializer
from ebook.models import EBook
from ebook.serializers import EBookSearchSerializer

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

@api_view(['POST', ])
@permission_classes((permissions.IsAuthenticated,))
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer, renderers.JSONRenderer])
def search_all(request):
    data = request.data
    search = data.get("search", None)

    atlases = Atlas.objects.all()
    books = Book.objects.all()
    infos = Infographic.objects.all()
    ebooks = EBook.objects.all()

    if search:
        atlases = atlases.filter(name__icontains=search)[:3]
        books = books.filter(title__icontains=search)[:3]
        infos = infos.filter(name__icontains=search)[:3]
        ebooks = ebooks.filter(title__icontains=search)[:3]
    else:
        atlases = atlases[:3]
        books = books[:3]
        infos = infos[:3]
        ebooks = ebooks[:3]


    
    data={
        'atlas': AtlasSerializer(atlases, many=True).data,
        'book': BookSerializer(books, many=True).data,
        'info': InfoSerializer(infos, many=True).data,
        'ebook': EBookSearchSerializer(ebooks, many=True).data,
    }
    return JsonResponse(data=data)
