from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Book, BookOrder, BookShopItem
from utils.admin import BaseAdmin


class BookAdmin(BaseAdmin):
    list_display = ('id', 'title', 'author', 'price', 'img', 'img_url', 'is_active', 'removed')
    list_editable = ()

    def img(self, obj):
        if obj.image:
            return mark_safe("<img width=50 height=50 src={}>".format(obj.image_url))
        else:
            return "No Image"
    
    def img_url(self, obj):
        return mark_safe("<a href={}>دانلود</>".format(obj.image_url))
    
    img.short_description = 'عکس'
    img_url.short_description = 'دانلود عکس'

class BookOrderAdmin(BaseAdmin):
    list_display = ('id', 'state', '_items')
    list_filter = ('state', )

    def _items(self, obj):
        html = ""
        for item in obj.items.all():
            html += '<p><a href="%s">%s</a></p>' %(item.get_admin_url(), item.__str__())
        return mark_safe(html)

class BookItemAdmin(BaseAdmin):
    list_display = ('id', 'book', 'quantity')

admin.site.register(Book, BookAdmin)
admin.site.register(BookShopItem, BookItemAdmin)
admin.site.register(BookOrder, BookOrderAdmin)
