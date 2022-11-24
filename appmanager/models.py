# appmanager/models.py
from django.db import models


class Run(models.Model):
    # todo: set defaults and fix datatypes
    # fix size of lengthes
    app_name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    # or parameters
    envs = models.CharField(max_length=200)
    status = models.CharField(max_length=8)
    # set field datetime
    time = models.CharField(max_length=200)

    def __str__(self):
        return self.app_name
