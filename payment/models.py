from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import BaseModel
from utils.payment import *

class Gateway(BaseModel):
    name = models.CharField(max_length=100, default="")
    unique_code = models.CharField(max_length=15, default="")
    img_url = models.CharField(max_length=400, default="")
    is_active = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)
    is_in_mobile_visible = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("درگاه")
        verbose_name_plural = _("درگاه‌ها")

    def __str__(self):
        return "%s-%s" % (self.unique_code, self.type)

    def __init__(self, *args, **kwargs):
        super(Gateway, self).__init__(*args, **kwargs)
        if self.unique_code:
            self.__class__ = payment.get_gateway_map().get(self.unique_code)

    def request_pay(self, *args, **kwargs):
        raise NotImplementedError

    def validate_pay(self, *args, **kwargs):
        raise NotImplementedError
