from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('catalog', views.index, name='catalog'),
]