from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Book
from utils.admin import BaseAdmin


class BookAdmin(BaseAdmin):
    list_display = ('id', 'title', 'author', 'price', 'img_url',)

    def img_url(self, obj):
        if obj.image:
            return mark_safe("<img src={}>".format(obj.image.url))
        else:
            return "No Image"
    
    img_url.short_description = 'Image url'

admin.site.register(Book, BookAdmin)