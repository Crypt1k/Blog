from django.views import generic
from account.forms import RegisterForm
from django.contrib.auth import authenticate, login


class RegisterView(generic.CreateView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        new_user = authenticate(username=self.request.POST['username'],
                                password=self.request.POST['password'])
        login(self.request, new_user)
        return super(RegisterView, self).form_valid(form)
