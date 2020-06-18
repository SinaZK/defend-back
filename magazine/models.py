from django.db import models
from utils.ftp import *
from utils.models import BaseModel
from utils.utils import code_generator

class MagazineCategory(BaseModel):
    title = models.CharField(max_length=255, blank=True, default='')
    image = models.FileField(null=True, blank=True, upload_to=UploadToPathAndRename(FTP_PUBLIC_DIR + "magazines"))

    @property
    def image_url(self):
        if self.image:
            return FTP_BASE_URL + self.image.name.replace(FTP_PUBLIC_DIR, '')
        return ''

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "دسته مجله"
        verbose_name_plural = "دسته مجله"

class Magazine(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True, default='')
    author = models.CharField(max_length=255, blank=True, null=True, default='')
    description = models.TextField(blank=True, null=True, default='')
    price = models.IntegerField(default=0) # Price in Toman
    image = models.FileField(null=True, blank=True, upload_to=UploadToPathAndRename(FTP_PUBLIC_DIR + "magazines"))
    dl_file = models.FileField(null=True, blank=True, upload_to=UploadToPathAndRename(FTP_PUBLIC_DIR + "magazines"))
    is_active = models.BooleanField(default=True)
    year = models.IntegerField(default=1390)
    number = models.IntegerField(default=1)
    category = models.ForeignKey("magazine.MagazineCategory", verbose_name="magazines", on_delete=models.CASCADE, default=None, blank=True, null=True)

    class Meta:
        verbose_name = "مجله"
        verbose_name_plural = "مجله‌ها"

    @property
    def file_url(self):
        if self.dl_file:
            return FTP_BASE_URL + self.dl_file.name.replace(FTP_PUBLIC_DIR, '')
        return ''

    @property
    def image_url(self):
        if self.image:
            return FTP_BASE_URL + self.image.name.replace(FTP_PUBLIC_DIR, '')
        return ''

    def has_purchased(self, user):
        if self.price == 0:
            return True

        purchases = MagazineOrder.objects.filter(member=user, magazine=self, state='paid')
        return len(purchases) > 0

state_choices = [
    ('checkout', 'Checkout'),
    ('paid', 'Paid'),
]

class MagazineOrder(BaseModel):
    state = models.CharField(max_length=30, choices=state_choices, default='checkout')
    member = models.ForeignKey('users.Member', on_delete=models.CASCADE, null=True, blank=True)
    magazine = models.ForeignKey('magazine.Magazine', on_delete=models.CASCADE, null=True, blank=True)
    token = models.CharField(max_length=30, default=code_generator)

    class Meta:
        verbose_name = "فاکتور خرید"
        verbose_name_plural = "فاکتورهای خرید"

    @property
    def pay_url(self): # generate at create view
        return "http://google.com"
