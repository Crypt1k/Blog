from django.views import generic
from userAuth.forms import RegisterForm
from django.contrib.auth import authenticate, login


class RegisterView(generic.CreateView):
    template_name = 'userAuth/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        new_user = authenticate(username=self.request.POST['username'],
                                password=self.request.POST['password'])
        login(self.request, new_user)
        form.save()
        return super(RegisterView, self).form_valid(form)
