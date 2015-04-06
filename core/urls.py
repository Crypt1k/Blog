from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
admin.site.site_header = 'Cryptic\'s blog admin'

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('account.urls', namespace='account')),
    url(r'^', include('app.urls', namespace='app')),
)
