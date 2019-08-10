from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News
from utils.admin import BaseAdmin


class NewsAdmin(BaseAdmin):
    list_display = ('id', 'img', 'title', 'is_show', 'img_url', 'created')
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

admin.site.register(News, NewsAdmin)