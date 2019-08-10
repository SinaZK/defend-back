from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Book
from utils.admin import BaseAdmin


class BookAdmin(BaseAdmin):
    list_display = ('id', 'title', 'author', 'price', 'img', 'img_url', 'removed')

    def img(self, obj):
        if obj.image:
            return mark_safe("<img src={}>".format(obj.image.url))
        else:
            return "No Image"
    
    def img_url(self, obj):
        return mark_safe("<a href={}>دانلود</>".format(obj.image_url))
    
    img.short_description = 'عکس'
    img_url.short_description = 'دانلود عکس'

admin.site.register(Book, BookAdmin)