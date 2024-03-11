from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('order', views.order),
    path('add', views.add),
    path('otziv', views.otziv),
    path('<int:pk>/delete', views.ServiceDeleteView.as_view(), name='task-delete'),
    path('<int:pk>/update', views.ServiceUpdateView.as_view(), name='task-update'),
]