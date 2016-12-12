from django import forms
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from accounts.models import UserProfile

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control'}) , label=_("Email"), required=True ,)
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}) , label=_("username") , required=True , min_length=6)
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'} ), label=_("password") , required=True)
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'} ), label=_("confirmation") , required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    avatar    = forms.FileField()
    class Meta:
        fields = ['avatar']
        model = UserProfile
