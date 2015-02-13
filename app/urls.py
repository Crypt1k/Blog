from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
from app.views import ArticleListView, ArticleYearView, ArticleMonthView, ArticleDayView, ArticleDetailView

urlpatterns = patterns(
    '',
    url(r'^$',
        login_required(ArticleListView.as_view()), name='article_list'),
    url(r'^(?P<year>\d{4})/$',
        login_required(ArticleYearView.as_view()), name='article_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/$',
        login_required(ArticleMonthView.as_view()), name='archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$',
        login_required(ArticleDayView.as_view()), name='article_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[-_\w]+)/$',
        login_required(ArticleDetailView.as_view()), name='article_detail'),
)