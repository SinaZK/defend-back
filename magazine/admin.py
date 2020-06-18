from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Magazine, MagazineOrder, MagazineCategory
from utils.admin import BaseAdmin


class MagazineAdmin(BaseAdmin):
    list_display = ('id', 'title', 'author', 'price', 'img', 'img_url', 'file_url','is_active')
    list_editable = ()

    def img(self, obj):
        if obj.image:
            return mark_safe("<img width=50 height=50 src={}>".format(obj.image_url))
        else:
            return "No Image"
    
    def img_url(self, obj):
        return mark_safe("<a href={}>دانلود عکس</>".format(obj.image_url))

    def file_url(self, obj):
        return mark_safe("<a href={}>دانلود فایل</>".format(obj.file_url))
    
    img.short_description = 'عکس'
    img_url.short_description = 'دانلود عکس'
    file_url.short_description = 'دانلود فایل'

class MagazineOrderAdmin(BaseAdmin):
    list_display = ('id', 'state', )
    list_filter = ('state', )

class MagazineCategoryAdmin(BaseAdmin):
    list_display = ('id', 'title', 'img_url')
    list_filter = ('title', )

    def img(self, obj):
        if obj.image:
            return mark_safe("<img width=50 height=50 src={}>".format(obj.image_url))
        else:
            return "No Image"
    
    def img_url(self, obj):
        return mark_safe("<a href={}>دانلود عکس</>".format(obj.image_url))

    img.short_description = 'عکس'
    img_url.short_description = 'دانلود عکس'

admin.site.register(Magazine, MagazineAdmin)
admin.site.register(MagazineOrder, MagazineOrderAdmin)
admin.site.register(MagazineCategory, MagazineCategoryAdmin)
