
# appmanager/serializers.py

from rest_framework import serializers
from appmanger import models


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        'name',
        'image',
        'envs',
        'time',
        'status',
    )
    model = models.Run
