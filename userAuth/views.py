from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from userAuth.forms import RegisterForm


def register_view(request):
    #user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword', first_name='fn', last_name='ln')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/myapp')
    else:
        form = RegisterForm()
    return render(request, 'userAuth/register.html', {'form': form})
