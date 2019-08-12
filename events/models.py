from khayyam import JalaliDate
from django.db import models
from django.utils import timezone

from utils.models import BaseModel
from utils.ftp import *

class Event(BaseModel):
    title = models.CharField(max_length=300, blank=True, default='')
    body = models.TextField(blank=True, default='')
    location = models.TextField(default='', blank=True)
    date = models.DateField(default=timezone.now)
    time = models.TimeField()
    image = models.FileField(upload_to=UploadToPathAndRename(FTP_PUBLIC_DIR + "events"), null=True, blank=True)

    class Meta:
        verbose_name = 'رویداد'
        verbose_name_plural = 'رویداد‌ها'

    def __str__(self):
        return self.title
    

    @property
    def jalali_date(self):
        return JalaliDate(self.date).__str__().replace("-", "/")

    @property
    def image_url(self):
        if self.image:
            return FTP_BASE_URL + self.image.name.replace(FTP_PUBLIC_DIR, '')
        return ''

