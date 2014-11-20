from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
from app.views import IndexView

urlpatterns = patterns('',
    url(r'^$', login_required(IndexView.as_view())),
)