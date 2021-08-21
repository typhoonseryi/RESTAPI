from django.db import models
from jsonfield import JSONField


class Item(models.Model):

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    params = JSONField()
