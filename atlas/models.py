from django.db import models
from utils.models import BaseModel
from mptt.models import MPTTModel, TreeForeignKey

from utils.ftp import *

class AtlasCategory(MPTTModel, BaseModel):
    name = models.CharField(max_length=250)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    class MPTTMeta:
        order_insertion_by = ['id']

    def __str__(self):
        return self.name
    

class Atlas(BaseModel):
    name = models.CharField(max_length=250, blank=True)
    body = models.TextField(blank=True)
    image = models.FileField(upload_to=UploadToPathAndRename(FTP_PUBLIC_DIR + "atlas"), null=True, blank=True)
    video = models.FileField(upload_to=UploadToPathAndRename(FTP_PUBLIC_DIR + "atlas"), null=True, blank=True)
    category = models.ForeignKey(AtlasCategory, on_delete=models.CASCADE ,related_name='atlases')

    class Meta:
        verbose_name = 'سامانه‌'
        verbose_name_plural = 'سامانه‌ها'
    
    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image:
            return FTP_BASE_URL + self.image.name.replace(FTP_PUBLIC_DIR, '')
        return ''

    @property
    def video_url(self):
        if self.video:
            return FTP_BASE_URL + self.video.name.replace(FTP_PUBLIC_DIR, '')
        return ''
