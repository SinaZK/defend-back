from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from django.contrib import admin

from utils.admin import BaseAdmin
from .models import AtlasCategory, Atlas

class AtlasCategoryAdmin(DraggableMPTTAdmin):
    pass
    #list_display = ('id', 'name',)

class AtlasAdmin(BaseAdmin):
    list_display = ('id', 'name', 'category')


admin.site.register(Atlas, AtlasAdmin)
admin.site.register(AtlasCategory, AtlasCategoryAdmin)
