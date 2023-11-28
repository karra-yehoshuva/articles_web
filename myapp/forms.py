from django import forms
from .models import Article
from django.contrib.auth.models import User

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

class ArticlecreateForm(forms.Form):

    title = forms.CharField(
        label= "Enter Title",
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'title',
                'class':'form-control'
            }

        )
    )

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder' : 'body',
                'class':'form-control',
                'rows': 10,
                'columns': 10
            }
        )
    )


class ArticleEditForm(forms.Form):

    title = forms.CharField(
        label= "Enter Title",
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'title',
                'class':'form-control'
            }

        )
    )

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder' : 'body',
                'class':'form-control',
                'rows': 10,
                'columns': 10
            }
        )
    )

class LoginForm(forms.Form):
    username = forms.CharField(
        label='USERNAME',
        widget=forms.TextInput(
            attrs={
                'placeholder':'username',
            'class':'form-control'
            }

        )
              
    )
    password = forms.CharField(
        label='PASSWORD',
        widget=forms.PasswordInput(

            attrs={

            'placeholder':'password',
            'class':'form-control'

            }

        )
            
    )

class UserRegisterForm(forms.ModelForm):
    
    password = forms.CharField(
        label ='password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password',
                'class':'form-control'
            }
        )
    )

    confirm_password = forms.CharField(
        label ='password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password',
                'class':'form-control'
            }
        )
    )
  
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username']

    # class Meta:
    #     model = Article
    #     fields = ('title','body')


