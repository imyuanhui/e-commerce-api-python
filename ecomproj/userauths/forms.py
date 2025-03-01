from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from userauths.models import User

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']

# class UserSigninForm(AuthenticationForm):

#     class Meta:
#         model = User
#         fields = ['username', 'email']