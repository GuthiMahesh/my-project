from django.shortcuts import render, redirect
from .models import UserRegistration


def Registration(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"register":type})


def login(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"login":type})


def Homepage(request):
    return render(request,"index.html")


def userdetails(request):
    name=request.POST.get("t1")
    cno=request.POST.get("t2")
    email=request.POST.get("t3")
    password=request.POST.get("t4")
    res=UserRegistration(name=name,contact_no=cno,email_id=email,password=password)
    res.save()
    return render(request,"index.html",{"msg":"saved Details"})


def loginvalidate(request):
    name = request.POST.get("m1")
    password = request.POST.get("m2")
    us = UserRegistration.objects.filter(name=name,password=password)
    if us:
        return render(request,"index.html")
    else:
        type = request.GET.get("type")
        return render(request, "index.html", {"register": type})


