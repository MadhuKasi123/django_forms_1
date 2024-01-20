from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def display_topic(request):
    QLTO=TopicForm()
    d={'QLTO':QLTO}
    if request.method=='POST':

        QLDO=TopicForm(request.POST)
        if QLDO.is_valid():
            tn=QLDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('topic is created')
        else:
            return HttpResponse('invalid data')






    return render (request,'display_topic.html',d)

def display_webpage(request):
    QLWO=WebpageForm()
    d1={"QLWO":QLWO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            
            nm=WFDO.cleaned_data['name']
            ur=WFDO.cleaned_data['url']
            WL=Topic.objects.get(topic_name=tn)
            
            WO=Webpage.objects.get_or_create(topic_name=WL,name=nm,url=ur)[0]
            WO.save()
            return HttpResponse('webpage object is create')
        else:
            return HttpResponse('invalid data')




    return render (request,'display_webpage.html',d1)