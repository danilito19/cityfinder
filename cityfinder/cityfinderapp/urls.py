from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.preferences, name='preferences'),
    url(r'^priorities/$', views.priorities, name='priorities'),
]
