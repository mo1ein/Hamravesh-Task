
# appmanager/views.py

import docker
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import RunSerializer
from appmanager import models


class CreateRun(generics.CreateAPIView):
    queryset = models.Run.objects.all()
    serializer_class = RunSerializer


class RunList(generics.ListAPIView):
    queryset = models.Run.objects.all()
    serializer_class = RunSerializer
