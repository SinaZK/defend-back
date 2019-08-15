# Generated by Django 2.1.5 on 2019-08-15 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0017_auto_20190814_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookorder',
            name='billing_address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bookorder',
            name='billing_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='bookorder',
            name='billing_phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='bookorder',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookshopitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='book.BookOrder', verbose_name='order'),
        ),
    ]