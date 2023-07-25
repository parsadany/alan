from django.db import models

# Create your models here.


class Cache(models.Model):
    json = models.JSONField(blank=True, null=True, default=None)
    text = models.TextField(blank=True, null=True, default=None)
