from django.db import models
from utils.models import BaseModel
from utils.ftp import *

class Book(BaseModel):

    title = models.CharField(max_length=255, blank=True, null=True, default='')
    author = models.CharField(max_length=255, blank=True, null=True, default='')
    description = models.TextField(blank=True, null=True, default='')
    price = models.IntegerField(default=0) # Price in Toman
    image = models.ImageField(null=True, blank=True, upload_to='books/')

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
            return FTP_BOOKS_URL + self.image.name
        return ''
