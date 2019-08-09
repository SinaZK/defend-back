from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Member
from utils.admin import BaseUserAdmin

class MemberAdmin(BaseUserAdmin, DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),

        #(_('Chests'), {'fields': ('chest1_is_empty')}),

        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),

        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('id', 'username', 'phone_number')
    list_filter = ('is_staff', 'last_login', 'created')
    search_fields = ('phone_number', 'id')
    ordering = ('-date_joined',)

admin.site.register(Member, MemberAdmin)
