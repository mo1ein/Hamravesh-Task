
# apps/views.py
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response

from appmanager import models
from .serializers import AppSerializer

from subprocess import call


def home_view(request, *args, **kwargs):
    return HttpResponse("<center><h1>HamRaveshTask</h1></center>")


class AppList(generics.ListAPIView):
    queryset = models.App.objects.all()
    get_serializer = AppSerializer


class AppDetail(generics.RetrieveAPIView):
    queryset = models.App.objects.all()
    get_serializer = AppSerializer


class CreateApp(generics.CreateAPIView):
    queryset = models.App.objects.all()
    get_serializer = AppSerializer


class DeleteApp(generics.RetrieveDestroyAPIView):
    queryset = models.App.objects.all()
    get_serializer = AppSerializer


class UpdateApp(generics.RetrieveUpdateAPIView):
    queryset = models.App.objects.all()
    get_serializer = AppSerializer

    def update(self, request, *args, **kwargs):
        # Partial update of the data
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # self.perform_update(serializer)
        else:
            return Response({"message": "failed", "details": serializer.errors})
        return Response(serializer.data)


class RunApp(generics.RetrieveAPIView):
    queryset = models.App.objects.all()
    get_serializer = AppSerializer
    data = models.App.objects.all().values()[0]
    print("===")
    print(data)
    command = f"docker run {data['image']} {data['command']}"
    # add if envs is not empty...
    # command = f"docker run -e {data[]} {data['command']}"


class RunAppList():
    queryset = models.App.objects.all()
    get_serializer = AppSerializer


class GetApp():
    queryset = models.App.objects.all()
    serializer_class = AppSerializer
