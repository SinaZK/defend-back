import pytz
from khayyam import *
from django.db import models
from utils.models import BaseModel
from utils.ftp import *

class News(BaseModel):
    title = models.CharField(max_length=300, default='', blank=True)
    body = models.TextField(default='', blank=True)
    video = models.FileField(null=True, blank=True, upload_to=UploadToPathAndRename(FTP_PUBLIC_DIR + "news"))
    image = models.FileField(null=True, blank=True, upload_to=UploadToPathAndRename(FTP_PUBLIC_DIR + "news"))
    is_show = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'

    @property
    def time(self):
        tehran = pytz.timezone('Asia/Tehran')
        return self.created.astimezone(tehran).time().strftime("%H:%M")
    
    @property
    def date(self):
        return JalaliDate(self.created).__str__()

    @property
    def image_url(self):
        if self.image:
            return FTP_BASE_URL + self.image.name.replace(FTP_PUBLIC_DIR, '')
        return ''

    @property
    def video_url(self):
        if self.video:
            return FTP_BASE_URL + self.image.name.replace(FTP_PUBLIC_DIR, '')
        return ''
