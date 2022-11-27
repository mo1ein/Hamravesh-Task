# apps/models.py

from django.db import models
from django.core.validators import RegexValidator


class App(models.Model):
    name = models.CharField(max_length=200)
    # validate image url format
    image = models.CharField(
        max_length=200,
        validators=[
            RegexValidator(
                regex=r'^(?:(?=[^:\/]{1,253})(?!-)[a-zA-Z0-9-]{1,63}(?<!-)(?:\.(?!-)[a-zA-Z0-9-]{1,63}(?<!-))*(?::[0-9]{1,5})?/)?((?![._-])(?:[a-z0-9._-]*)(?<![._-])(?:/(?![._-])[a-z0-9._-]*(?<![._-]))*)(?::(?![.-])[a-zA-Z0-9_.-]{1,128})?$',
                message='image is not valid',
                code='invalid_url'
            )
        ]
    )
    # todo: must be list
    envs = models.CharField(max_length=200)
    command = models.CharField(max_length=200)

    def __str__(self):
        return self.name
