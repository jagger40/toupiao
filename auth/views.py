# -*- coding: utf-8 -*-  
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Account
from .forms import LoginForm,RegistForm
from django.http.response import  HttpResponseRedirect

def login(request):
    if request.method == 'POST':
        
        form = LoginForm(request.POST)
        if form.is_valid():
            
            data = form.cleaned_data
            a = Account.objects.get(email = data['email'])
            request.session['account'] = a
            return HttpResponseRedirect('/touke/')
        
    else:
        
        form = LoginForm()
        
    return render_to_response('auth/login.html',{'form':form},context_instance=RequestContext(request))

def singup(request):
    
    if request.method == 'POST':
        
        form = RegistForm(request.POST)
        if form.is_valid():
            
            data = form.cleaned_data
            account = Account(email=data['email'],username=data['username'],password=data['password1'],is_active=True,avatar=None)
            account.save()
    
    else:
        
        form = RegistForm()
        
    return render_to_response('auth/singup.html',{'form':form},context_instance=RequestContext(request))
        
        
    
    
    
