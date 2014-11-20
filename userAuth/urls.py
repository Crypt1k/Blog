from django.conf.urls import patterns, url
from userAuth.views import RegisterView

urlpatterns = patterns('',
    url(r'^$', RegisterView.as_view(), name='register'),
)