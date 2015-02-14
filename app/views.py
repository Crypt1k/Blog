from django.views import generic
from app.models import Article


class ArticleListMixin(object):
    model = Article
    template_name = 'app/article_list.html'
    context_object_name = 'articles'
    paginate_by = 2
    date_field = 'pub_date'
    allow_empty = True


class ArticleListView(ArticleListMixin, generic.ArchiveIndexView):
    pass


class ArticleYearView(ArticleListMixin, generic.YearArchiveView):
    make_object_list = True


class ArticleMonthView(ArticleListMixin, generic.MonthArchiveView):
    month_format = '%m'


class ArticleDayView(ArticleListMixin, generic.DayArchiveView):
    month_format = '%m'


class ArticleDetailView(generic.DateDetailView):
    model = Article
    template_name = 'app/article_detail.html'
    context_object_name = 'article'
    date_field = 'pub_date'
    month_format = '%m'

