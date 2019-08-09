from django.db import models

class Magazine(models.Model):
    title = models.CharField(max_length=255, blank=True, default='')
    description = models.TextField(blank=True, default='')
    price = models.IntegerField(default=0) # Price in Tomans

