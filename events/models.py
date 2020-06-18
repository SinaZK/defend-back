from khayyam import JalaliDate
from django.db import models
from django.utils import timezone
import datetime

from utils.models import BaseModel
from utils.ftp import *

type_choices = [
    ('regular', 'Regular'),
    ('thesis', 'Thesis'),
]

class Event(BaseModel):
    title = models.CharField(max_length=300, blank=True, default='')
    body = models.TextField(blank=True, default='')
    location = models.TextField(default='', blank=True)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=datetime.time(12, 00))
    end_date = models.DateField(default=timezone.now)
    end_time = models.TimeField(default=datetime.time(12, 00))
    info = models.CharField(max_length=300, blank=True, default='')
    image = models.FileField(upload_to=UploadToPathAndRename(FTP_PUBLIC_DIR + "events"), null=True, blank=True)
    user_event = models.BooleanField(default=False)
    admin_approved = models.BooleanField(default=False)
    user = models.ForeignKey("users.Member", on_delete=models.CASCADE, null=True, default=None, blank=True)
    # Tez Defend Fields:
    type = models.CharField(max_length=30, choices=type_choices, default='Regular')
    student_name = models.CharField(max_length=300, blank=True, default='')
    teacher_name = models.CharField(max_length=300, blank=True, default='')
    university = models.CharField(max_length=300, blank=True, default='')

    class Meta:
        verbose_name = 'رویداد'
        verbose_name_plural = 'رویداد‌ها'

    def __str__(self):
        return self.title
    
    @property
    def jalali_date(self):
        return JalaliDate(self.date).__str__().replace("-", "/")

    @property
    def jalali_end_date(self):
        return JalaliDate(self.end_date).__str__().replace("-", "/")

    @property
    def image_url(self):
        if self.image:
            return FTP_BASE_URL + self.image.name.replace(FTP_PUBLIC_DIR, '')
        return ''

