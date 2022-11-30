
# appmanager/views.py

import docker
from appmanager.models import Run
from django.shortcuts import render
from rest_framework import generics
from .serializers import RunSerializer
from rest_framework.response import Response


class RunList(generics.ListAPIView):
    queryset = Run.objects.all()
    serializer_class = RunSerializer

    # check containers are running? or finished?
    def get(self, request, *args, **kwargs):
        runs = self.queryset.values()
        client = docker.from_env()
        running_containers = client.containers.list()
        container_names = [c.name for c in running_containers]
        for run in runs:
            if run['container_name'] not in container_names:
                data = run
                data['status'] = 'finished'
                pk = run['id']
                instance = Run.objects.get(pk=pk)
                serializer = self.serializer_class(
                    instance,
                    data=data,
                    partial=True
                )
                if serializer.is_valid():
                    serializer.save()
        queryset = self.get_queryset()
        serializer = RunSerializer(queryset, many=True)
        return Response(serializer.data)
