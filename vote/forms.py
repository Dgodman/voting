from django import forms
from django.contrib.auth.models import User
from vote.models import UserInfo
from votelist import us_states


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ProfileForm(forms.ModelForm):
    state_home = forms.CharField(widget=forms.Select(choices=us_states), max_length=2, disabled=True)

    class Meta:
        model = UserInfo
        fields = ('state_home',)


class StateForm(forms.ModelForm):
    state_home = forms.CharField(widget=forms.Select(choices=us_states), max_length=2)

    class Meta:
        model = UserInfo
        fields = ('state_home',)