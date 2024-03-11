from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView, DetailView, View
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import SignUpForm, LoginFrom
from .models import User
from prototypes.models import Prototype



class IndexView(TemplateView):
    """ ホームビュー """
    template_name = "index.html"


class SignupView(CreateView):
    """ ユーザー登録用ビュー """
    form_class = SignUpForm # 作成した登録用フォームを設定
    template_name = "accounts/signup.html" 
    success_url = reverse_lazy("prototypes:list") # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        user = authenticate(email=email, password=password)
        login(self.request, user)
            
        return response

signup = SignupView.as_view()


class LoginView(LoginView):
    form_class = LoginFrom
    template_name = "accounts/login.html"

login = LoginView.as_view()


class LogoutView(LogoutView):
    next_page = 'prototypes:list'

logout = LogoutView.as_view()


class UserDetail(View):
    def get(self, request, *args, **kwargs):
        user_id = self.kwargs['pk']
        user = User.objects.get(pk=user_id)
        prototypes = Prototype.objects.filter(user__id = user_id)
        return render(request, 'accounts/detail.html', {'user': user, 'prototypes': prototypes})