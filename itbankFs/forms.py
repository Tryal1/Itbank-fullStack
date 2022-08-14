from django import forms


class loginForm(forms.Form):
    dni = forms.CharField(required=True,
                          widget=forms.TextInput(attrs={'class': 'imput-text', 'placeholder': 'DNI'}))
    password = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'imput-text', 'placeholder': 'Password'}))
    pin = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'imput-text', 'placeholder': 'Password'}))
