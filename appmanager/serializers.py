
# appmanager/serializers.py

from rest_framework import serializers
from appmanager import models


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'app_name',
            'image',
            'envs',
            'status',
            'time',
        )
        model = models.Run
