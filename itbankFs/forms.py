from django import forms


class loginForm(forms.Form):
    user = forms.CharField(required=True,
                          widget=forms.TextInput(attrs={'class': 'imput-text', 'placeholder': 'User'}))
    password = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'imput-text', 'placeholder': 'Password'}))
    pin = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'imput-text', 'placeholder': 'Pin'}))

class RegisterForm(forms.Form):
    user = forms.CharField(required=True,
                          widget=forms.TextInput(attrs={'class': 'imput-text', 'placeholder': 'User'}))
    password = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'imput-text', 'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'imput-text', 'placeholder': 'Repeat Password'}))
    pin = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'imput-text', 'placeholder': 'Pin'}))

