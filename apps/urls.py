
# apps/urls.py
from django.urls import path
from .views import AppList, AppDetail, UpdateApp, DeleteApp, RunApp

urlpatterns = [
    path('', AppList.as_view()),
    path('<int:pk>/', AppDetail.as_view()),
    path('<int:pk>/update', UpdateApp.as_view()),
    path('<int:pk>/delete', DeleteApp.as_view()),
    path('<int:pk>/run', RunApp.as_view()),
]
