from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

admin.autodiscover()
admin.site.site_header = 'Cryptic\'s blog admin'

urlpatterns = i18n_patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('account.urls', namespace='account')),
    url(r'^', include('app.urls', namespace='app')),
)
