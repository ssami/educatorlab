from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

from django.contrib import admin
admin.autodiscover()

dajaxice_autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mainlab.views.index'),
	url(r'^browse/$', 'mainlab.views.browse'),
	url(r'^curriculum/i=(?P<id>\d+)/$', 'mainlab.views.curriculum'),
	url(r'^grade/i=(?P<id>\d+)/$', 'mainlab.views.grade'),
	url(r'^subject/i=(?P<id>\d+)/$', 'mainlab.views.subject'),
	url(r'^chapter/i=(?P<id>\d+)/$', 'mainlab.views.chapter'),
	url(r'^activity/i=(?P<id>\d+)&c=(?P<cid>\d+)/$', 'mainlab.views.activity'),
	url(r'^project/i=(?P<id>\d+)&c=(?P<cid>\d+)/$', 'mainlab.views.project'),
	url(r'^about/$', 'mainlab.views.about'),  
  	url(r'^submit_resource/$', 'mainlab.views.submit_resource'),
	url(r'^suggest/$', 'mainlab.views.suggest'),
	url(r'^managerAdmin/$', 'mainlab.views.managerAdmin'),
	url(r'^manager/$', 'mainlab.views.manager'),
	url(r'^activityEdit/i=(?P<id>\d+)/$', 'mainlab.views.activityEdit'),
	url(r'^projectEdit/i=(?P<id>\d+)/$', 'mainlab.views.projectEdit'),
	url(r'^saveActivity/$', 'mainlab.views.saveActivity'),
	url(r'^saveProject/$', 'mainlab.views.saveProject'),
	url(r'^deleteActivity/$', 'mainlab.views.deleteActivity'),
	url(r'^deleteProject/$', 'mainlab.views.deleteProject'),
	url(r'^sendEmail/$', 'mainlab.views.sendEmail'),
	# Admin and Grappelli
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
	(r'^grappelli/', include('grappelli.urls')),
	(r'^tinymce/', include('tinymce.urls')),
	# Dajaxice
	url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
	#Login Stuff
	url(r'^account/', include('django.contrib.auth.urls')),
	url(r'^user/password/reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    (r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/user/password/done/'}),
    (r'^user/password/done/$', 
        'django.contrib.auth.views.password_reset_complete'),
)
