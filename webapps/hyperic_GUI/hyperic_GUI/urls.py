from django.conf.urls import patterns, include, url
from hyperic_GUI import views
from django.contrib.auth.decorators import login_required
from hyperic_GUI import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^logout/$', views.logout, name='logout'),
		url(r'^applogic/$', views.applogic, name='applogic'),
		url(r'/applogic/', views.applogic, name='applogic'),
		url(r'^tojson/$', views.applogic, name='tojson'),
		(r'^resources/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	)

# Examples:
# url(r'^$', 'hyperic_GUI.views.home', name='home'),
# url(r'^hyperic_GUI/', include('hyperic_GUI.foo.urls')),
# Uncomment the admin/doc line below to enable admin documentation:
# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
# Uncomment the next line to enable the admin:
# url(r'^admin/', include(admin.site.urls)),
