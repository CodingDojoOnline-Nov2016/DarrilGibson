from django.conf.urls import url

# use for favicon
from django.views.generic.base import RedirectView

from . import views

favicon_view = RedirectView.as_view(url='/static/surveyform/graphics/home.jpg', permanent=True)

urlpatterns = [
    url(r'^favicon\.ico$', favicon_view),
    url(r'^$', (views.index)),
    url(r'^process$', views.process),
    url(r'^results$', views.results),
]
