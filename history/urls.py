from django.urls import path
from . import views


app_name = 'history'
urlpatterns = [
    path('', views.index, name='index'),
    path('export_users_xls', views.export_users_xls, name='export_users_xls'),
]
