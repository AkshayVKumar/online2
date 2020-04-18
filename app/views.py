from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from app.models import *
import populate
from django.db.models import Q
# Create your views here.
def index(request):
    if request.method=="POST":
        return render(request,"form_demo.html",context={'value':request.POST.get("username")})
        
    return render(request,"form_demo.html")

def radio(request):
    return render(request,"radio.html")

def checkbox(request):
    if request.method=="POST" :
        print(request.POST.getlist("gender"))
        return HttpResponse("selected gender is \"{}\"".format(request.POST.getlist("gender")))
    return render(request,"checkbox.html")

def select(request):
    if request.method=="POST":
        return HttpResponse("selected country is \"{}\"".format(request.POST.getlist("country")))
    return render(request,"select.html")

def radio_output(request):
    print("Control in radio output")
    return HttpResponse("selected gender is \"{}\"".format(request.GET.get("gender")))

import os
def file_demo(request):
    img_url=None
    if request.method=="POST" and request.FILES['profile']:
        profile_pic=request.FILES['profile']
        fs=FileSystemStorage(location=os.path.join(settings.MEDIA_DIR,"images"))
        file_name=fs.save(profile_pic.name,profile_pic)
        img_url=fs.url(file_name)
                
    return render(request,"file_demo.html",context={'img_url':img_url})

def create_topic(request):
    if request.method=="POST":
        populate.add_topic(topic=request.POST['topic'])
        return HttpResponse("<h1> Topic Added Successfully </h1>")
    return render(request,'create_topic.html')

def create_webpage(request):
    if request.method=="POST":
        populate.add_webpage(request.POST['topic'],\
            request.POST['name'],request.POST['url'])
        return HttpResponse("<h1>webpage created successfully</h1>")
    topics=Topic.objects.all()
    return render(request,"create_webpage.html",\
        context={'topics':topics})    

def select_topic(request):
    d={'topics':Topic.objects.all()}
    if request.method=="POST":
        topic=request.POST['topic']
        #topic_obj=Topic.objects.get(topic=topic)
        #topic_obj=Topic.objects.get(topic__icontains=topic)
        topic_obj=Topic.objects.get(topic__istartswith=topic)
        return HttpResponse("<h1>{}</h1>".format(topic_obj.topic))
    return render(request,"select_topic.html",context=d)

def topic_select(request):
    d={'topics':Topic.objects.all()}
    return render(request,"topic_select.html",context=d)

def disp_web(request):
    topic_name=request.GET['topic']
    topic=Topic.objects.get(topic__icontains=topic_name)
    #d={"webpages":Webpage.objects.filter(~Q(topic=topic))}
    d={"webpages":Webpage.objects.exclude(topic=topic)}
    return render(request,"disp_web.html",d)


