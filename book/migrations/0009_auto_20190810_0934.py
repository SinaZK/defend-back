# Generated by Django 2.1.5 on 2019-08-10 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_remove_book_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='public_html/books/'),
        ),
    ]