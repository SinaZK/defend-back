# Generated by Django 2.1.5 on 2019-08-09 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image_url',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
    ]
