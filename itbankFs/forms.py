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
    email = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'imput-text', 'placeholder': 'email'}))
    
    
class Prestamos(forms.Form):
    cantidad = forms.CharField(required=True,
                          widget=forms.TextInput(attrs={'class': 'imput-text', 'placeholder': 'Cantidad'}))
    motivo = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'imput-text', 'placeholder': 'Motivo'}))
    dni = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'imput-text', 'placeholder': 'Dni'}))
    pin = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'imput-text', 'placeholder': 'Pin'}))

