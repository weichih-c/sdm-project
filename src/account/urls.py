from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
]
