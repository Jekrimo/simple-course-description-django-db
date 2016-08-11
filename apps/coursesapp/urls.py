from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^courses/destroy/(?P<id>\d+)$', views.confirm),
    url(r'^kill/(?P<id>\d+)$', views.kill)
]
