from django.views.generic import CreateView
from .models import CustomUser
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterCustomUserForm

# Create your views here.


class RegisterView(CreateView):
    model = CustomUser
    form_class = RegisterCustomUserForm
    template_name = 'authenticate_app/register.html'
    success_url = '/authenticate/login/'


class LoginUserView(LoginView):
    template_name = 'authenticate_app/login.html'
    success_url = '/'

    # def post(self, request, *args, **kwargs):
    #     import pdb
    #     pdb.set_trace()


class LogoutView(LogoutView):
    redirect_field_name = 'poster'
