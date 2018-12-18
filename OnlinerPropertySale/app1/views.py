from django.shortcuts import render

from app1.models import UserRegistration,Property


def Registration(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"register":type,"type":"register"})


def login(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"type":type})


def Homepage(request):
    return render(request,"index.html")


def userdetails(request):
    return render(request,"index.html",{"message":"saved Details","login":"registered","type":"register"})



def loginvalidate(request):
    name = request.POST.get("m1")
    password = request.POST.get("m2")
    us = UserRegistration.objects.filter(name=name,password=password)
    if us:
        return render(request,"welcome.html")
    else:
        type = request.GET.get("type")
        return render(request, "login.html", {"message":"Invalid user name and password","type":type})


def welcomeuser(request):
    name = request.POST.get("m1")
    password = request.POST.get("m2")
    ur = UserRegistration.objects.get(email_id=name,password=password)
    if ur:
        return render(request,"welcome.html",{"emp":ur})
    else:
        return render(request,"login.html",{"message":"Invalid user name and password"})


def registeruser(request):
    name=request.POST.get("t1")
    cno=request.POST.get("t2")
    email=request.POST.get("t3")
    password=request.POST.get("t4")
    res=UserRegistration(name=name,contact_no=cno,email_id=email,password=password)
    res.save()
    return render(request,"index.html",{"type":"login"})


def viewprofile(request):
    email=request.GET.get('uname')
    us=UserRegistration.objects.get(email_id=email)
    return render(request,"welcome.html",{"emp":us,"type":"profile"})


def AddProperties(request):
    email = request.GET.get('email')
    res = UserRegistration.objects.get(email_id=email)
    from .models import Property
    # prodetails = property.objects.filter(Customer_Email=email)
    return render(request, "welcome.html", {"type": "add_property", "emp":res,"udetails": res})


def update(request):
    email=request.GET.get("email")
    res=UserRegistration.objects.get(email_id=email)
    type="mahesh"
    return render(request,"welcome.html",{"res":res,"emp":res,"type":type})


def perssion(request):
    name=request.POST.get("name")
    con=request.POST.get("contact")
    email=request.POST.get("email")
    password=request.POST.get("password")
    mahi=UserRegistration(name=name,contact_no=con,email_id=email,password=password)
    mahi.save()
    type='mahesh'
    emp=UserRegistration.objects.get(email_id=email)
    return render(request,"welcome.html",{"type":type,"msge":"updated","emp":emp})


def add_property_user(request):
    name=request.POST.get("name")
    con=request.POST.get("contact")
    img=request.POST.get("image")
    email=request.POST.get("email")
    state=request.POST.get("state")
    city=request.POST.get("city")
    price=request.POST.get("price")
    res=Property(name=name,contact_number=con,state=state,city=city,image=img,Email=email,price=price)
    res.save()
    return render(request,"welcome.html",{"msg":"Data Saved"})
