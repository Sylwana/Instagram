from django.shortcuts import render
from django.views.generic import FormView, CreateView, UpdateView, ListView, DeleteView
from .models import User
from .forms import UserLoginForm


# Create your views here.
class UserCreateView(FormView):
    model = User
    form_class = UserLoginForm
    template_name = 'Igers/login_form.html'