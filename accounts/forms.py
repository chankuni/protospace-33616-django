from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2", "username", "profile", "occupation", "position")

# ログインフォームを追加
class LoginFrom(AuthenticationForm):
    class Meta:
        model = User

    # email = forms.EmailField(
    #     required=True
    # )
        




