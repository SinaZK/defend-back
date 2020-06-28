from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin, TreeNodeChoiceField
from django.contrib import admin
from django import forms
from django.views.decorators.csrf import csrf_exempt                                          
#@csrf_exempt 

from utils.admin import BaseAdmin
from .models import AtlasCategory, Atlas

#class AtlasCategoryAdmin(DraggableMPTTAdmin):
#   pass

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

class AtlasCatAdmin(BaseAdmin):
    actions = ['delete_model']

    def get_actions(self, request):
        actions = super(AtlasCatAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def delete_model(self, request, obj):
        print("hello")
        for o in obj.all():
            print("deleteing: ", o)
            o.delete()
    delete_model.short_description = 'Delete flow'

    def get_queryset(self, request):
        return super().get_queryset(request).filter(removed=None)

admin.site.register(Atlas, AtlasAdmin)
admin.site.register(AtlasCategory, AtlasCatAdmin)
