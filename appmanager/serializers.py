
# appmanager/serializers.py

from rest_framework import serializers
from appmanager import models


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'app_name',
            'image',
            'container_name',
            'envs',
            'status',
            'created_at',
        )
        model = models.Run
