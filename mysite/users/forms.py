from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# RegisterForm is a custom user registration form that extends Django's built-in UserCreationForm.
class RegisterForm(UserCreationForm):
    # Adds an email field to the registration form.
    email = forms.EmailField()

    # The Meta class defines additional options for the form.
    class Meta:
        # Specifies the model to use, which is the default User model provided by Django.
        model = User
        # Specifies the fields to be included in the form, in the order they should appear.
        fields = ['username', 'email', 'password1', 'password2']
