from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import BaseModel
from utils.ftp import *
from utils.utils import code_generator

class EBook(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True, default='')
    author = models.CharField(max_length=255, blank=True, null=True, default='')
    description = models.TextField(blank=True, null=True, default='')
    price = models.IntegerField(default=0) # Price in Toman
    image = models.FileField(null=True, blank=True, upload_to=UploadToPathAndRename(FTP_PUBLIC_DIR + "ebooks"))
    dl_file = models.FileField(null=True, blank=True, upload_to=UploadToPathAndRename(FTP_PUBLIC_DIR + "ebooks"))
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "EBook"
        verbose_name_plural = "EBooks"

    def __str__(self):
        return "{}-{}".format(self.title, self.author)

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})
    
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

state_choices = [
    ('checkout', 'Checkout'),
    ('paid', 'Paid'),
]

class EBookOrder(BaseModel):
    state = models.CharField(max_length=30, choices=state_choices, default='checkout')
    member = models.ForeignKey('users.Member', on_delete=models.CASCADE, null=True, blank=True)
    ebook = models.ForeignKey('ebook.Ebook', on_delete=models.CASCADE, null=True, blank=True)
    token = models.CharField(max_length=30, default=code_generator)

    @property
    def pay_url(self): # generate at create view
        return "http://google.com"
