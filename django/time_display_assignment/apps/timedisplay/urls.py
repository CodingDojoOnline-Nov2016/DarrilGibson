from django.conf.urls import url
# from . import (dot means current folder)
from . import views

urlpatterns = [
    url('^$', views.index),
]
