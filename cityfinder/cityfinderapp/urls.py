from django.conf.urls import patterns, url, include
from . import views
#  from django.views.generic import TemplateView
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	url(r'^$', views.priorities, name='priorities'),
	url(r'^preferences/$', views.preferences, name='preferences'),
	url(r'^city_results/$', views.city_results, name='city_results'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

