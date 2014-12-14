from django.conf.urls import patterns, url
from account.views import RegisterView

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'account/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'account/logged_out.html'}, name='logout'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change',
        {'template_name': 'account/password_change_form.html', 'post_change_redirect': 'account:password_change_done'}
        , name='password_change'),
    url(r'^password_change_done/$', 'django.contrib.auth.views.password_change_done',
        {'template_name': 'account/password_change_done.html'}, name='password_change_done'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset',
        {'template_name': 'account/password_reset_form.html', 'post_reset_redirect': 'account:password_reset_done'},
        name='password_reset'),
    url(r'^password_reset_done/$', 'django.contrib.auth.views.password_reset_done',
        {'template_name': 'account/password_reset_done.html'}, name='password_reset_done'),
    url(r'^complete/$', 'django.contrib.auth.views.password_reset_complete',
        name='password_reset_complete'),
    url(r'^confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^registration/$', RegisterView.as_view(), name='register'),
)