from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'account/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'account/logged_out.html'}, name='logout'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change',
        {'template_name': 'account/password_change_form.html'}, name='password_change'),
    url(r'^password_change_done/$', 'django.contrib.auth.views.password_change_done',
        {'template_name': 'account/password_change_done.html'}, name='password_change_done'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset',
        {'template_name': 'account/password_reset_form.html'}, name='password_reset'),
    url(r'^password_reset_done/$', 'django.contrib.auth.views.password_reset_done',
        {'template_name': 'account/password_reset_done.html'}, name='password_reset_done'),
    url(r'^register/$', include('account.urls', namespace='account')),
    url(r'^', include('app.urls', namespace='app')),
)

urlpatterns += staticfiles_urlpatterns()