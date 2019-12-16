from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin, TreeNodeChoiceField
from django.contrib import admin
from django import forms

from utils.admin import BaseAdmin
from .models import InfographicCategory, Infographic

class InfoCategoryAdmin(DraggableMPTTAdmin):
    pass

class InfoAdminForm(forms.ModelForm):
    category = TreeNodeChoiceField(queryset=InfographicCategory.objects.all())

    class Meta:
        model = Infographic
        exclude = []

class InfoAdmin(BaseAdmin):
    form=InfoAdminForm
    list_display = ('id', 'name', 'root_category', 'category')

    def root_category(self, obj):
        return obj.category.get_root()


admin.site.register(Infographic, InfoAdmin)
admin.site.register(InfographicCategory, InfoCategoryAdmin)
