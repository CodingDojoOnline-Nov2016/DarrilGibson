from django.conf.urls import url
from . import views
from django.contrib import admin

# use for favicon
from django.views.generic.base import RedirectView
favicon_view = RedirectView.as_view(url='/static/gold/images/smile.jpg', permanent=True)

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_money$', views.process_money),
]
