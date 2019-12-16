from django.db import models
from utils.models import BaseModel
from mptt.models import MPTTModel, TreeForeignKey

from utils.ftp import *

class InfographicCategory(MPTTModel, BaseModel):
    name = models.CharField(max_length=250)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    class MPTTMeta:
        order_insertion_by = ['id']

    def __str__(self):
        return self.name
    

class Infographic(BaseModel):
    name = models.CharField(max_length=250, blank=True)
    top_text = models.TextField(blank=True)
    bottom_text = models.TextField(blank=True)
    image = models.FileField(upload_to=UploadToPathAndRename(FTP_PUBLIC_DIR + "info"), null=True, blank=True)
    category = models.ForeignKey(InfographicCategory, on_delete=models.CASCADE ,related_name='infos')

    class Meta:
        verbose_name = 'داده‌نگاری'
        verbose_name_plural = 'داده‌نگاری‌ها'
    
    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image:
            return FTP_BASE_URL + self.image.name.replace(FTP_PUBLIC_DIR, '')
        return ''
