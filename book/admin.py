from django.contrib import admin
from .models import Book
from utils.admin import BaseAdmin


class BookAdmin(BaseAdmin):
    list_display = ('id', 'title', 'author', 'price')

admin.site.register(Book, BookAdmin)