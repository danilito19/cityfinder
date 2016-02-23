from django.conf.urls import patterns, url, include
from . import views
#  from django.views.generic import TemplateView
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

'''
Error we get due to url patterns:  need to resolve this
Users/dani/Desktop/cityfinder/cityfinder/cityfinderapp/urls.py:6: 
RemovedInDjango110Warning: django.conf.urls.patterns() is deprecated 
and will be removed in Django 1.10. Update your urlpatterns to be a 
list of django.conf.urls.url() instances instead.

'''
# urlpatterns = patterns('', url(r'^$', TemplateView.as_view(template_name='priorities.html'), name="home"))

# urlpatterns += patterns('', url(r'^preferences$', TemplateView.as_view(template_name='preferences.html'), name="preferences"))

# urlpatterns += staticfiles_urlpatterns() #only for testing

urlpatterns = [
	url(r'^$', views.priorities, name='priorities'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# url(r'^priorities/$', views.priorities, name='priorities'),