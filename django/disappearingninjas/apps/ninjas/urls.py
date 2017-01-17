from django.conf.urls import url
from . import views
# use for favicon
from django.views.generic.base import RedirectView
favicon_view = RedirectView.as_view(url='/static/ninjas/graphics/homer.png', permanent=True)

urlpatterns = [
    url(r'^favicon\.ico$', favicon_view),
    url(r'^$', views.index),
    # catch the color first
    url(r'^ninjas/(?P<color>[a-zA-Z]+)$', views.ninjacolor ),
    # [/]? indicates with a slash or without a slash
    # if I put this first, it would catch the colors too.
    url(r'^ninjas[/]?$', views.ninjas),

]
