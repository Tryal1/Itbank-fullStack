from django import forms

class loginForm(forms.Form):

    dni = forms.CharField(label='DNI', required=True)

    password = forms.CharField(label='PASSWORD', required=True)

    password = forms.NumberInput(label='PIN', required=True)

    

    