from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import re

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Mot de passe")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirmer le mot de passe")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).{8,}$', password):
            raise ValidationError('Le mot de passe doit contenir au moins 8 caractères, incluant une majuscule, une minuscule et un caractère spécial.')
        return password

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password1") != cleaned_data.get("password2"):
            raise ValidationError("Les mots de passe ne correspondent pas.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    


    from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']
