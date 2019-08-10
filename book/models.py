import os
from uuid import uuid4
from django.db import models
from django.utils.deconstruct import deconstructible

from utils.models import BaseModel
from utils.ftp import *

@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        print(instance.id, "file", filename)
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.sub_path, filename)

class Book(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True, default='')
    author = models.CharField(max_length=255, blank=True, null=True, default='')
    description = models.TextField(blank=True, null=True, default='')
    price = models.IntegerField(default=0) # Price in Toman
    image = models.ImageField(null=True, blank=True, upload_to=UploadToPathAndRename("public_html/books"))
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return "{}-{}".format(self.title, self.author)

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})
    
    @property
    def image_url(self):
        if self.image:
            return FTP_BASE_URL + self.image.name.replace('public_html/', '')
        return ''
