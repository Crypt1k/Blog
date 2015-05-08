from django.conf import settings
from django.views import generic
from django.db.models import Q
try:
    from functools import reduce
except ImportError:
    pass
import operator
from app.models import Article


class ArticleListMixin(object):
    model = Article
    template_name = 'app/article_list.html'
    context_object_name = 'articles'
    paginate_by = 5
    allow_empty = True


class ArticleListView(ArticleListMixin, generic.ListView):
    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        if self.request.GET.get('search'):
            context.update({
                'extra_param': 'search=' + self.request.GET.get('search', None)
            })
        return context

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            q1 = reduce(operator.and_,
                        (Q(headline__icontains=x) for x in search.split(' ')))
            q2 = reduce(operator.and_,
                        (Q(content__icontains=x) for x in search.split(' ')))
            return Article.objects.filter(q1 | q2)
        else:
            return Article.objects.all()


class ArticleLabelView(ArticleListMixin, generic.ListView):
    def get_context_data(self, **kwargs):
        context = super(ArticleLabelView, self).get_context_data(**kwargs)
        context.update({'label_filter': True})
        return context

    def get_queryset(self):
        return Article.objects.filter(labels__name=self.kwargs.get('name'))


class ArticleYearView(ArticleListMixin, generic.YearArchiveView):
    date_field = 'pub_date'
    make_object_list = True


class ArticleMonthView(ArticleListMixin, generic.MonthArchiveView):
    date_field = 'pub_date'
    month_format = '%m'


class ArticleDayView(ArticleListMixin, generic.DayArchiveView):
    date_field = 'pub_date'
    month_format = '%m'


class ArticleDetailView(generic.DateDetailView):
    model = Article
    context_object_name = 'article'
    date_field = 'pub_date'
    month_format = '%m'

    def get_template_names(self):
        if 'disqus' in settings.INSTALLED_APPS:
            return 'app/article_detail_disqus.html'
        else:
            return 'app/article_detail.html'
