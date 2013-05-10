# -*- coding: utf-8 -*-  
from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()

class RegisterForm(forms.Form):
    email = forms.EmailField(label="邮箱地址",max_length=30,widget=forms.TextInput(attrs={'size':30,}))
    password=forms.CharField(label=_(u"密码"),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,}))  
    username=forms.CharField(label=_(u"昵称"),max_length=30,widget=forms.TextInput(attrs={'size': 20,})) 