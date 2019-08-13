from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin, TreeNodeChoiceField
from django.contrib import admin
from django import forms

from utils.admin import BaseAdmin
from .models import AtlasCategory, Atlas

class AtlasCategoryAdmin(DraggableMPTTAdmin):
    pass

class AtlasAdminForm(forms.ModelForm):
    category = TreeNodeChoiceField(queryset=AtlasCategory.objects.all())

    class Meta:
        model = Atlas
        exclude = []

class AtlasAdmin(BaseAdmin):
    form=AtlasAdminForm
    list_display = ('id', 'name', 'root_category', 'category')

    def root_category(self, obj):
        return obj.category.get_root()


admin.site.register(Atlas, AtlasAdmin)
admin.site.register(AtlasCategory, AtlasCategoryAdmin)
