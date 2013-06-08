from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mainlab.views.home', name='home'),
    # url(r'^mainlab/', include('mainlab.foo.urls')),
    url(r'^$', 'mainlab.views.index'),
	url(r'^browse/$', 'mainlab.views.browse'),
	url(r'^curriculum/i=(?P<id>\d+)/$', 'mainlab.views.curriculum'),
	url(r'^grade/i=(?P<id>\d+)/$', 'mainlab.views.grade'),
	url(r'^subject/i=(?P<id>\d+)/$', 'mainlab.views.subject'),
	url(r'^chapter/i=(?P<id>\d+)/$', 'mainlab.views.chapter'),
	url(r'^activity/i=(?P<id>\d+)&c=(?P<cid>\d+)/$', 'mainlab.views.activity'),
	url(r'^project/i=(?P<id>\d+)&c=(?P<cid>\d+)/$', 'mainlab.views.project'),
	url(r'^organizer/i=(?P<id>\d+)&c=(?P<cid>\d+)/$', 'mainlab.views.organizer'),
	url(r'^foldable/i=(?P<id>\d+)/$', 'mainlab.views.foldable'),
	url(r'^graphicorganizer/i=(?P<id>\d+)/$', 'mainlab.views.graphicOrganizer'),
	url(r'^about/$', 'mainlab.views.about'), 
	#url(r'^contrib_form/$', 'mainlab.views.contrib'), 
  	url(r'^submit_resource/$', 'mainlab.views.submit_resource'),
  # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	(r'^grappelli/', include('grappelli.urls')),
	(r'^tinymce/', include('tinymce.urls')),
	#dajaxice
	url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)
