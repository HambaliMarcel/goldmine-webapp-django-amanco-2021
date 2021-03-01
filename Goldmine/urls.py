from django.contrib import admin
from django.urls import path, include

from . import views

# this is Main URLS on root (Goldmine)
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('engine/', include('engine.urls', namespace='engine')),
    path('history/', include('history.urls', namespace='history')),
    path('settings/', include('settings.urls', namespace='settings')),
]
