from django.urls import path

from . import views

app_name = 'engine'

urlpatterns = [
    path('', views.index, name='index'),
    path('addnewsource/', views.addnewsource, name='ans'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
]
