from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@login_required()
def index_view(request):
    data = 'Welcome to my blog!'
    return render(request, 'app/index.html', {'data': data})