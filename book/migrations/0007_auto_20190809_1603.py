# Generated by Django 2.1.5 on 2019-08-09 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20190809_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='books/'),
        ),
    ]
