
# apps/serializers.py
from rest_framework import serializers
from apps import models


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'image',
            'envs',
            'command',
        )
        model = models.App
