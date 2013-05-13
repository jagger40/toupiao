# -*- coding:utf-8 -*-
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from .models import Account

class LoginForm(forms.Form):
    '''
        登录验证表单对象
    '''
    email = forms.EmailField(
                             label='邮箱地址',
                             widget=forms.TextInput(attrs={'placeholder':'电子邮箱地址'})
    )
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_password(self): 
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
      
        try:
            a = Account.objects.get(email = email)
            if a.password != password:
                raise forms.ValidationError('帐号密码不匹配')
        except ObjectDoesNotExist:
            raise forms.ValidationError('不存在的帐号')
        return password
    
class RegistForm(forms.Form):
    '''
        注册验证表单
    '''
    username = forms.CharField(label=u'用户名',max_length=30)
    email = forms.EmailField(u'邮箱')
    
    password1 = forms.CharField(
                               label=u'密码',
                               widget=forms.PasswordInput()
    )
    
    password2 =  forms.CharField(
                               label=u'确认密码',
                               widget=forms.PasswordInput()
    )
    
    def clean_password2(self):
        ''' 
            检查两次密码是否一致
        '''
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            
            if password1 == password2:
                return password2
            
            raise forms.ValidationError('两次密码不一致')
        
    def clean_email(self):
        
        email =  self.cleaned_data['email']
        try:
            a = Account.objects.get(email = email)
        except Account.DoesNotExist:
            return email
            
        raise forms.ValidationError('邮箱已注册')

