from django.views import generic
from app.models import Article


class IndexView(generic.ListView):
    model = Article
    template_name = 'app/index.html'
    context_object_name = 'articles'
    paginate_by = 2
