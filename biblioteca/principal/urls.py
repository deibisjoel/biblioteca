from django.conf.urls import patterns, include, url

from principal import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#url(r'^$', views.inicio, name='inicio'),

	url(r'^$', views.index), 

	url(r'media/(?P<path>.*)','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
	)