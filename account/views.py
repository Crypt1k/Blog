from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from account.forms import RegisterForm


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('app:article_list')

    def form_valid(self, form):
        result = super(RegisterView, self).form_valid(form)
        new_user = authenticate(username=self.request.POST['username'],
                                password=self.request.POST['password1'])
        login(self.request, new_user)
        return result
