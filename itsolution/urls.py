from django.urls import path
from . import views


urlpatterns = [
    path('pollos', views.index, name='index')
]
