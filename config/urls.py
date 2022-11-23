
# config/urls.py
from django.contrib import admin
from django.urls import include, path
from apps.views import CreateApp, home_view

urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('apps/', include('apps.urls')),
    path('create', CreateApp.as_view())
    # path('run', RunAppList.as_view())
]
