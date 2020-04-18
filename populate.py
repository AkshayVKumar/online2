import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',"P.settings")

import django
django.setup()

from faker import Faker
import random
from app.models import *

f=Faker()
topics=["Music","sports","Social Media","Games","video","Bank"]
def add_topic(topic):
    t=Topic.objects.get_or_create(topic=topic)[0]
    t.save()
    return t

def add_webpage(topic,name,url):
    t=add_topic(topic)
    w=Webpage.objects.get_or_create(topic=t,name=name,url=url)[0]
    w.save()
    return w

def add_access(topic,name,url,date):
    w=add_webpage(topic,name,url)
    a=Access_Details.objects.get_or_create(web_name=w,date=date)[0]
    a.save()

if __name__=='__main__':
    n=int(input("Enter the number of records "))
    print("populating is started")
    for i in range(n):
        topic=random.choice(topics)
        name=f.name()
        url=f.url()
        date=f.date()
        add_access(topic,name,url,date)
    print("populating is done")