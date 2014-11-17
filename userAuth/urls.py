from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$',  'userAuth.views.register_view'),
)