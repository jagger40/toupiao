# -*- coding: utf-8 -*-  
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from touke.models import Poll,Choice,Comment,Account
from django.http import Http404,HttpResponse,HttpResponseRedirect
from .forms import CreatePollForm
from datetime import datetime 

def index(request):
    return render_to_response("index.html",context_instance=RequestContext(request))

# Create your views here.
def findChoice(request):
   
    last_poll_list = Poll.objects.all().order_by('-pub_date')
    return render_to_response("touke/findchoice.html",
          {'last_poll_list':last_poll_list},
          context_instance=RequestContext(request)
    )

def PollDetail(request,poll_id):
    
    '''
        GET choice 详情页面
        POST 提交评论
    '''
    p = get_object_or_404(Poll,pk=poll_id)
    if request.method == 'GET':
        
        choices = p.choice_set.all()
        comment = p.comment_set.all()
        if "voted_"+str(poll_id) in request.COOKIES:
            return render_to_response("touke/item.html",
                {"poll":p,"choices":choices,"comments":comment,"voted":True},
                context_instance=RequestContext(request)
            )
        else:
            return render_to_response("touke/item.html",
                {"poll":p,"choices":choices,"comments":comment},
                context_instance=RequestContext(request)
            )
    else:
        
        account=  request.session['account']
        text = request.POST['comment'];
        comment = Comment(text=text,poll=p,account=account)
        comment.save();
        return HttpResponseRedirect('/touke/'+poll_id+'/#choice-comment')

def vote(request,poll_id):
    '''  投票 ''' 
    p = get_object_or_404(Poll,pk=poll_id)
    try:
        select_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        raise Http404
    else:
        select_choice.votes += 1
        select_choice.save()
        result = '{"choice":'+str(select_choice.id)+',"vote":'+str(select_choice.votes)+'}'
        response = HttpResponse(result);
        response.set_cookie("voted_"+str(p.id),"true")
        
        return response; 
    
def home(request,member_id):
    
    account = get_object_or_404(Account,pk=member_id)
    polls = account.poll_set.all()
    return render_to_response("touke/home.html",{'account':account,'polls':polls}, context_instance=RequestContext(request))

def create(request):
    
    if request.method == 'POST':
        
        form = CreatePollForm(request.POST)
        if form.is_valid():
            
            data = form.cleaned_data
            poll = Poll(account= request.session['account'],question=data['question'],story=data['story'],keyword=data['keyword'],visted=0,pub_date= datetime.now())
            poll.save()
           
            return render_to_response("touke/create.html", {'form':form},context_instance=RequestContext(request))
           
    else:
        
        form = CreatePollForm()
        
    return render_to_response("touke/create.html", {'form':form},context_instance=RequestContext(request))
    
    
