from django.conf.urls import patterns, url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	url(r'^$', views.priorities, name='priorities'),
	url(r'^preferences_citysize/$', views.preferences_citysize, name='preferences_citysize'),
	url(r'^preferences_weather/$', views.preferences_weather, name='preferences_weather'),
	url(r'^preferences_community/$', views.preferences_community, name='preferences_community'),
	url(r'^city_results/$', views.city_results, name='city_results'),
	url(r'^error/$', views.error, name='error'),
	url(r'^about/$', views.about, name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

