from django.conf.urls import patterns, url, include
from . import views
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('', url(r'^$', TemplateView.as_view(template_name='priorities.html'), name="home"))

urlpatterns += patterns('', url(r'^preferences/', TemplateView.as_view(template_name='preferences.html'), name="preferences"))

urlpatterns += staticfiles_urlpatterns() #only for testing

#url(r'^$', views.preferences, name='preferences'),
#url(r'^priorities/$', views.priorities, name='priorities'),