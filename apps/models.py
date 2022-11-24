# appmanager/models.py
from django.db import models


class App(models.Model):
    # todo: set defaults
    # fix size of lengthes
    name = models.CharField(max_length=200)
    # must be url type ...
    # image = models.URLField(max_length=200)
    image = models.CharField(max_length=200)
    # todo: must be list
    envs = models.CharField(max_length=200)
    command = models.CharField(max_length=200)

    def __str__(self):
        return self.name

