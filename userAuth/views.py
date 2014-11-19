from django.shortcuts import render
from django.http import HttpResponseRedirect
from userAuth.forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render(request, 'userAuth/register.html', {'form': form})
