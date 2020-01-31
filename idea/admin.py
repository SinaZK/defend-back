from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Idea
from utils.admin import BaseAdmin

class IdeaAdmin(BaseAdmin):
    list_display = ('id', 'title', 'state', 'state_text', 'user', 'code')
    list_editable = ()
    list_filter = ('state',)
    search_fields = ('id', 'code', 'title')

admin.site.register(Idea, IdeaAdmin)
