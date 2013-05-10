# -*- coding: utf-8 -*-  
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.http.response import Http404
from django.template import RequestContext
from choice.models import Member 

def index(request):
   
    return render_to_response("index.html",context_instance=RequestContext(request))

def auth(request):
    return render_to_response("auth.html",context_instance=RequestContext(request))

def login(request):
    if request.method!='POST':
        raise Http404('Only POST are allowed')
    try:
        m = Member.objects.get(email=request.POST['email'])
        if m.password == request.POST['password']:
            request.session['user'] = m
            return HttpResponseRedirect('/touke')
    except Member.DoesNotExist:
        return HttpResponse("your username and password didn't macth")
    else:
        return HttpResponse("error")
    
def logout(request):
   
    try:
        del request.session['user']
    except KeyError:
        pass
    return HttpResponseRedirect('/auth/')

    