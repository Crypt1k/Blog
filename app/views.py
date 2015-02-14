from django.views import generic
from app.models import Article


class ArticleListView(generic.ArchiveIndexView):
    model = Article
    template_name = 'app/article_list.html'
    context_object_name = 'articles'
    paginate_by = 2
    date_field = 'pub_date'


class ArticleYearView(generic.YearArchiveView):
    model = Article
    template_name = 'app/article_list.html'
    context_object_name = 'articles'
    paginate_by = 2
    date_field = 'pub_date'
    make_object_list = True


class ArticleMonthView(generic.MonthArchiveView):
    model = Article
    template_name = 'app/article_list.html'
    context_object_name = 'articles'
    paginate_by = 2
    date_field = 'pub_date'
    month_format = '%m'


class ArticleDayView(generic.DayArchiveView):
    model = Article
    template_name = 'app/article_list.html'
    context_object_name = 'articles'
    paginate_by = 2
    date_field = 'pub_date'
    month_format = '%m'


class ArticleDetailView(generic.DateDetailView):
    model = Article
    template_name = 'app/article_detail.html'
    context_object_name = 'article'
    date_field = 'pub_date'
    month_format = '%m'

