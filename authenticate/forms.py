from django import forms

class loginForm(forms.Form):
    username = forms.CharField(label="Username" , widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'title': 'Username',
        'placeholder': 'Plese enter your username',
        'required': True,
    }))
    password = forms.CharField(label="Password", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Plese enter your password',
        'required': True,
    }))
