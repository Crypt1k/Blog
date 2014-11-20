from django.views.generic.edit import FormView
from userAuth.forms import RegisterForm


class RegisterView(FormView):
    template_name = 'userAuth/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)
