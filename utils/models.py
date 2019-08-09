import reversion
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_permanent.models import PermanentModel

from utils.managers import UserManager

@reversion.register()
class BaseModel(PermanentModel):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=20, blank=True, unique=False)
    handle = models.CharField(max_length=100, default="", blank=True)
    email = models.EmailField(_('email address'), blank=True, null=True, default="")
    birth_date = models.DateField(_('birth date'), null=True, blank=True, default=None)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        abstract = True

    def get_short_name(self):
        return self.handle

    def get_full_name(self):
        return self.handle

    def send_otp(self, raw_otp, joined):
        pass

    def __str__(self):
        return self.username
