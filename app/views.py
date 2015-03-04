from django.views import generic
from django.db.models import Q
from app.models import Article
try:
    from functools import reduce
except ImportError:
    pass
import operator


class ArticleListMixin(object):
    model = Article
    template_name = 'app/article_list.html'
    context_object_name = 'articles'
    paginate_by = 2
    date_field = 'pub_date'
    allow_empty = True


class ArticleListView(ArticleListMixin, generic.ArchiveIndexView):
    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        if self.request.GET.get('search'):
            context.update({'extra_param': 'search=' + self.request.GET.get('search', None)})
        return context

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            q1 = reduce(operator.and_, (Q(headline__icontains=x) for x in search.split(' ')))
            q2 = reduce(operator.and_, (Q(content__icontains=x) for x in search.split(' ')))
            return Article.objects.filter(q1 | q2)
        else:
            return Article.objects.all()


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

