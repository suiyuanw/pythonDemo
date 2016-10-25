from django.conf.urls import include, url
from django.conf.urls import patterns
from django.contrib import admin

urlpatterns = patterns('', 
		url(r'^admin/', include(admin.site.urls)),
		url(r'^blogs/', include('blogs.urls')),
		# url(r'^', include('blogs.urls'))
	) 
