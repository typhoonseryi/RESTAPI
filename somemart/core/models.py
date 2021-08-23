from djongo import models


class Item(models.Model):

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    params = models.JSONField()
