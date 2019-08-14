from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import BaseModel
from utils.ftp import *

class Book(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True, default='')
    author = models.CharField(max_length=255, blank=True, null=True, default='')
    description = models.TextField(blank=True, null=True, default='')
    price = models.IntegerField(default=0) # Price in Toman
    image = models.FileField(null=True, blank=True, upload_to=UploadToPathAndRename(FTP_PUBLIC_DIR + "books"))
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
            return FTP_BASE_URL + self.image.name.replace(FTP_PUBLIC_DIR, '')
        return ''

state_choices = [
    ('checkout', 'Checkout'),
    ('paid', 'Paid'),
    ('cancel', 'Canceled'),
    ('payfail', 'Paid Failed'),
    ('delivering', 'Delivering'),
    ('delivered', 'Delivered'),
]

class BookOrder(BaseModel):
    state = models.CharField(max_length=30, choices=state_choices, default='checkout')

    

class BookShopItem(BaseModel):
    book = models.ForeignKey("Book", verbose_name=_("book"), on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey("BookOrder", related_name='items', verbose_name=_("order"), on_delete=models.CASCADE, null=True, blank=True)

    def get_admin_url(self):
        return "/admin/book/bookshopitem/%d/" %self.id

    def __str__(self):
        return '{}-{}'.format(self.book, self.quantity)
