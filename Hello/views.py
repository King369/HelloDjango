from django.shortcuts import render
from  django.http import HttpResponse
import datetime,time

# Create your views here.
def sayHello(request):
    s="Hello Wrold"
    current_time=datetime.datetime.now()
    html="<h1>%s</h1><p>%s</p>"%(s,current_time)
    return HttpResponse(html)

def sayHello1(request):
    list=[{id:1,"name":"Jack"},{id:2,"name":"Rose"}]
    return render("Hello.html",{"Hellos":list})