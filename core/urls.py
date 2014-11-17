from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change',
        name='password_change'),
    url(r'^password_change_done/$', 'django.contrib.auth.views.password_change_done',
         name='password_change_done'),
    url(r'^password_reset/$',
        'django.contrib.auth.views.password_reset',
        name='password_reset'),
    url(r'^password_reset_done/$', 'django.contrib.auth.views.password_reset_done',
         name='password_reset_done'),
    url(r'^register/$', include('userAuth.urls', namespace='userAuth')),
    url(r'^', include('app.urls', namespace='app')),
)