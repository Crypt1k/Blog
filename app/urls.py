from django.conf.urls import patterns, url
from app.views import (ArticleListView, ArticleLabelView,
                       ArticleYearView, ArticleMonthView,
                       ArticleDayView, ArticleDetailView)

urlpatterns = patterns(
    '',
    url(r'^$',
        ArticleListView.as_view(), name='article_list'),
    url(r'^label/(?P<name>[-_\s\w]+)/$',
        ArticleLabelView.as_view(), name='article_label'),
    url(r'^(?P<year>\d{4})/$',
        ArticleYearView.as_view(), name='article_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/$',
        ArticleMonthView.as_view(), name='article_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$',
        ArticleDayView.as_view(), name='article_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[-_\w]+)/$',
        ArticleDetailView.as_view(), name='article_detail'),
)
