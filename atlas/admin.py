from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin, TreeNodeChoiceField
from django.contrib import admin
from django import forms
from django.views.decorators.csrf import csrf_exempt                                          
#@csrf_exempt 

from utils.admin import BaseAdmin
from .models import AtlasCategory, Atlas

class AtlasCategoryAdmin(DraggableMPTTAdmin):
   pass

class AtlasAdminForm(forms.ModelForm):
    category = TreeNodeChoiceField(queryset=AtlasCategory.objects.all())

    class Meta:
        model = Atlas
        exclude = []

class AtlasAdmin(admin.ModelAdmin):
    form=AtlasAdminForm
    list_display = ('id', 'name', 'root_category', 'category')

    def root_category(self, obj):
        return obj.category.get_root()

admin.site.register(Atlas, AtlasAdmin)
admin.site.register(AtlasCategory, AtlasCategoryAdmin)
