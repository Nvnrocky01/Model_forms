from django.shortcuts import render

# Create your views here.
from app.forms import *

def insert_topic(request):
    etfo=Topicform()
    d={'etfo':etfo}
    if request.method=='POST':
        tfdo=Topicform(request.POST)
        if tfdo.is_valid():
            tfdo.save()
            qlto=Topic.objects.all()
            d1={'topic':qlto}
            return render(request,'display_topic.html',d1)
    return render(request,'insert_topic.html',d)



def insert_webpage(request):
    ewfo=Webpageform()
    d={'ewfo':ewfo}
    if request.method=='POST':
        wfdo=Webpageform(request.POST)
        if wfdo.is_valid():
            wfdo.save()
            qlwo=Webpage.objects.all()
            d1={'webpage':qlwo}
            return render(request,'display_webpage.html',d1)
    return render(request,'insert_webpage.html',d)



def insert_accessrecord(request):
    eafo=accessrecordform()
    d={'eafo':eafo}
    if request.method=='POST':
        afdo=accessrecordform(request.POST)
        if afdo.is_valid():
            afdo.save()
            qlao=AcessRecord.objects.all()
            d1={'accessrecord':qlao}
            return render(request,'display_accessrecord.html',d1)
    return render(request,'insert_accessrecord.html',d)
