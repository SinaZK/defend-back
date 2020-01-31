from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Idea
from utils.admin import BaseAdmin

class IdeaAdmin(BaseAdmin):
    list_display = ('id', 'title', 'state', 'state_text', 'user')
    list_editable = ()

admin.site.register(Idea, IdeaAdmin)