from django.conf.urls import patterns, url
from account.views import RegisterView

urlpatterns = patterns('',
    url(r'^$', RegisterView.as_view(), name='register'),
)