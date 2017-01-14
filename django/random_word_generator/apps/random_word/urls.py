from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^generate$', views.generate),
]
