
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

    def get(self, request, *args, **kwargs):
        runs = self.queryset.values()
        client = docker.from_env()
        running_containers = client.containers.list()
        container_names = [c.name for c in running_containers]
        for run in runs:
            if run['container_name'] not in container_names:
                data = run
                data['status'] = 'finished'
                pk = request.data[run['container_name']]
                instance = models.Run.objects.get(pk=pk)
                q = models.Run(instance, data=data)
                q.save()
        return Response(data)
