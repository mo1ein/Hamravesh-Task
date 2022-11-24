# appmanager/models.py
from django.db import models


class Run(models.Model):
    # todo: set defaults and fix datatypes
    # fix size of lengthes
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    # or parameters
    envs = models.CharField(max_length=200)
    status = models.BooleanField()
    time = models.CharField(max_length=200)

    def __str__(self):
        return self.name
