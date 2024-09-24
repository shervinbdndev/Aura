from django import forms
from django.core import validators





class RegisterForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=64,
        required=True,  
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),    
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-4',
            'style': 'box-shadow: 0 4px 8px rgba(0, 0, 0 ,0.1)',
            'placeholder': 'Enter your username',
            'id': 'username',
        },),
    )
    
    first_name = forms.CharField(
        min_length=3,
        max_length=64,
        required=True,  
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),    
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-4',
            'style': 'box-shadow: 0 4px 8px rgba(0, 0, 0 ,0.1)',
            'placeholder': 'Enter your first name',
            'id': 'fname',
        },),
    )
    
    last_name = forms.CharField(
        min_length=3,
        max_length=64,
        required=True,  
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),    
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-4',
            'style': 'box-shadow: 0 4px 8px rgba(0, 0, 0 ,0.1)',
            'placeholder': 'Enter your last name',
            'id': 'lname',
        },),
    )
    
    email = forms.EmailField(
        max_length=150,
        required=True,
        validators=[
            validators.EmailValidator(),
        ],
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-4',
            'style': 'box-shadow: 0 4px 8px rgba(0, 0, 0 ,0.1)',
            'placeholder': 'Enter your email',   
            'id': 'email',
        },),
    )
    
    password = forms.CharField(
        min_length=6,
        max_length=64,
        required=True,
        label='Password (Include characters & numbers)',
        validators=[
            validators.MinLengthValidator(limit_value=6),
            validators.MaxLengthValidator(limit_value=64),
        ],
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-4',
            'style': 'box-shadow: 0 4px 8px rgba(0, 0, 0 ,0.1)',
            'placeholder': 'Enter your password',
            'id': 'pass',
        },),
    )
    
    con_password = forms.CharField(
        min_length=6,
        max_length=64,
        label='Confirm Passowrd',
        required=True,
        validators=[
            validators.MinLengthValidator(limit_value=6),
            validators.MaxLengthValidator(limit_value=64),
        ],
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-4',
            'style': 'box-shadow: 0 4px 8px rgba(0, 0, 0 ,0.1);',
            'placeholder': 'Confirm your password',
            'id': 'conpass',
        },),
    )




class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=64,
        label='Username',
        required=True,   
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),    
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-4',
            'style': 'box-shadow: 0 4px 8px rgba(0, 0, 0 ,0.1)',
            'placeholder': 'Enter your username',
            'id': 'username',
        },),
    )
    
    password = forms.CharField(
        min_length=6,
        max_length=64,
        label='Password',
        required=True,
        validators=[
            validators.MinLengthValidator(limit_value=6),
            validators.MaxLengthValidator(limit_value=64),
        ],
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-4',
            'style': 'box-shadow: 0 4px 8px rgba(0, 0, 0 ,0.1)',
            'placeholder': 'Enter your password',
            'id': 'pass'
        },),
    )