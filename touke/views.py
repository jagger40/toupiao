from django.shortcuts import render_to_response, get_object_or_404
from touke.models import Poll
# Create your views here.
def findChoice(request):
    last_poll_list = Poll.objects.all().order_by('-pub_date')
    return render_to_response("touke/findchoice.html",{'last_poll_list':last_poll_list})

def ChoiceDetail(request,choice_id):
    p = get_object_or_404(Poll,pk=choice_id)
    choices = p.choice_set.all()
    return render_to_response("touke/item.html",{"poll":p,"choices":choices})
