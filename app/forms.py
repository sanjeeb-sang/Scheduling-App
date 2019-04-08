from django import forms
from django.contrib.auth.models import User
from app.models import Suggestion
from django.contrib.auth.forms import UserCreationForm


TEXTFIELD_HTML_CLASS = "mdl-textfield__input change-form-background"


class SuggestionForm(forms.ModelForm):

    class Meta:

        model = Suggestion;

        fields = ['user_name', 'user_email', 'suggestion']

        widgets = {
                'user_name' : forms.TextInput(attrs={'class' : TEXTFIELD_HTML_CLASS}),
                'user_email' : forms.EmailInput(attrs={'class' : TEXTFIELD_HTML_CLASS}),
                'suggestion' : forms.Textarea(attrs={'class' : TEXTFIELD_HTML_CLASS}),
            }


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        widgets = {
                'username' : forms.TextInput(attrs={'class' : TEXTFIELD_HTML_CLASS}),
                'first_name' : forms.TextInput(attrs={'class' : TEXTFIELD_HTML_CLASS}),
                'last_name' : forms.TextInput(attrs={'class' : TEXTFIELD_HTML_CLASS}),
                'email' : forms.EmailInput(attrs={'class' : TEXTFIELD_HTML_CLASS}),
                'password1' : forms.PasswordInput(attrs={'class' : TEXTFIELD_HTML_CLASS}),
                'password2' : forms.PasswordInput(attrs={'class' : TEXTFIELD_HTML_CLASS}),
            }
