# appmanager/models.py
from django.db import models


class Run(models.Model):
    app_name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    envs = models.CharField(max_length=200)
    status = models.CharField(max_length=8)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.app_name
