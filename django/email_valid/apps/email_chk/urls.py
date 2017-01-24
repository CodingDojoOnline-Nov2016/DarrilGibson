from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^check_email$', views.check_email),
    url(r'^success$', views.success),
    url(r'^check_email/(?P<id>\d+)/delete', views.destroy),
]
