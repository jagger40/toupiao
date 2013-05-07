# -*- coding: utf-8 -*-  
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.http.response import Http404
from django.contrib import auth

def index(request):
    return render_to_response("index.html")

def auth(request):
    return render_to_response("auth.html")

def login(request):
    if request.method =='POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username = username,password=password)
        if user is not None and user.is_active:
            
            auth.login(request, user)
            #Redirect to success page
            return HttpResponseRedirect('/touke')
        else:
            return HttpResponseRedirect('/auth')
    else:
        #抛出404异常
        raise Http404
    
def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/auth")
    