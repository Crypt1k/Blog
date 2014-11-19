from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from app.models import Article


@login_required()
def index_view(request):
    articles = Article.objects.all()
    return render(request, 'app/index.html', {'article_list': articles})