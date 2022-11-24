# apps/views.py

import docker
from apps import models
from django.http import HttpResponse
from rest_framework import generics
from .serializers import AppSerializer
from rest_framework.response import Response
from appmanager.models import Run
from appmanager.serializers import RunSerializer


def home_view(request, *args, **kwargs):
    return HttpResponse("<center><h1>HamRaveshTask</h1></center>")


class AppList(generics.ListAPIView):
    queryset = models.App.objects.all()
    serializer_class = AppSerializer


class AppDetail(generics.RetrieveAPIView):
    queryset = models.App.objects.all()
    serializer_class = AppSerializer


class CreateApp(generics.CreateAPIView):
    queryset = models.App.objects.all()
    serializer_class = AppSerializer


class DeleteApp(generics.RetrieveDestroyAPIView):
    queryset = models.App.objects.all()
    serializer_class = AppSerializer


class UpdateApp(generics.RetrieveUpdateAPIView):
    queryset = models.App.objects.all()
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
    queryset = models.App.objects.all()
    serializer_class = AppSerializer
    data = queryset.values()[0]
    print(data)
    # todo: labels...
    name = data['name']
    # image = data['image']
    image = 'hub.hamdocker.ir/nginx:1.21'
    envs = data['envs']
    command = data['command'].split()

    client = docker.from_env()
    container = client.containers.run(image, command, detach=True)
    # add time
    q = Run(app_name=name, image=image, envs=envs, status='running', time="")
    q.save()

    '''
    container = client.containers.list(all=True)
    for i in container:
        # print(i.id, i.name, i.image, i.status)
        print(i.logs(timestamps=True))
    '''

class GetApp():
    queryset = models.App.objects.all()
    serializer_class = AppSerializer
