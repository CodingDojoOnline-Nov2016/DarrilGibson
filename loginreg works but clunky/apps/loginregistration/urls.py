from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$',views.login),
    url(r'^register$',views.register),
    url(r'^success$', views.success),
    url(r'^show$', views.show),
    url(r'^show/(?P<id>\d+)/delete$', views.destroy),
]