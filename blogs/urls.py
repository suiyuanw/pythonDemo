from django.conf.urls import url
from django.conf.urls import patterns
from . import views

urlpatterns = patterns('',
		url(r'^$', views.post_list, name='post_list'),
	)
