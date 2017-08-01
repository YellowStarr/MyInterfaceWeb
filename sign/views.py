# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from models import Testcase
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#首页入口，展示用例
def index(request):
    if request.method=="GET":
        c = selectCase()
        print c
        return render(request, 'index.html',{"case":c})
    elif request.method=="POST":
        r=request.POST.get("uname","")
        return render(request,"index.html",{'w':r})

def inserttestcase(request):
    if request.method=="GET":
        return render(request,"inserttestcase.html")
    elif request.method == "POST":
        name = request.POST.get("desc","")
        n=name.encode('utf-8')
        baseurl = request.POST.get("baseurl","")
        url = request.POST.get("url","")
        args = request.POST.get("args","")
        methods = request.POST.get("method","")
        # arg=eval(args)
        print "-----------"+baseurl
        r={"name":n,"baseurl":baseurl,"url":url,"args":args,'method':methods}
        # if not type(r):
        insertCase(r)
        return render(request, "inserttestcase.html")

def insertCase(data):
    case = Testcase(name=data['name'],baseurl=data['baseurl'],url=data['url'],args=data['args'],method=data['method'])
    case.save()
    print "insert"

def selectCase():
    cases = Testcase.objects.all()
    return cases