# apps/views.py

#!/bin/python3

import docker
import datetime
from apps.models import App
from appmanager.models import Run
from rest_framework import generics
from django.http import HttpResponse
from .serializers import AppSerializer
from rest_framework.response import Response
from appmanager.serializers import RunSerializer


def home_view(request, *args, **kwargs):
    return HttpResponse("<center><h1>HamRaveshTask</h1></center>")


class AppList(generics.ListAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer


class AppDetail(generics.RetrieveAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer


class CreateApp(generics.CreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer


class DeleteApp(generics.RetrieveDestroyAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer


class UpdateApp(generics.RetrieveUpdateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer

    def update(self, request, *args, **kwargs):
        # Partial update of the data
        instance = self.get_object()
        serializer = self.serializer_class(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # self.perform_update(serializer)
        else:
            return Response({"message": "failed", "details": serializer.errors})
        return Response(serializer.data)


class RunApp(generics.RetrieveAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer

    def get(self, request, *args, **kwargs):
        data = self.queryset.values()[0]
        app = data['name']
        image = data['image']
        envs = data['envs']
        command = data['command'].split()
        client = docker.from_env()
        try:
            container = client.containers.run(image, command, detach=True)
            container_name = container.name
            status = 'running'
            
            q = Run(
                    app_name=app,
                    image=image,
                    container_name=container_name,
                    envs=envs,
                    status=status,
                    created_at=datetime.datetime.now(datetime.timezone.utc)
            )
            q.save()

            run_data = {
                    'name': app,
                    'image': image,
                    'container_name': container_name,
                    'envs': envs,
                    'status': status
            }

            return Response(run_data)
        except:
            return Response({"message": "faild to run container"})