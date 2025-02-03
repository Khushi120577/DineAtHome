from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from userapp.models import User
from userapp import forms
from userapp import models
from adminapp import views


# Create your views here.

def aboutview(request):
    return render(request,'userapp/about.html')

def blogview(request):
    return render(request,'userapp/blog.html')

def blogdetailview(request):
    return render(request, 'userapp/blogdetail.html')

def bookingview(request):
    return render(request,'userapp/booking.html')

def chefview(request):
    return render(request,'userapp/chef.html')

def contactview(request):  
    return render(request,'userapp/contact.html')


def featureview(request):
    return render(request,'userapp/feature.html')

def indexview(request):
    return render(request,'userapp/index.html')

def loginview(request):
      if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None and user.role == "Chef":
            login(request,user)
            return redirect(indexview)
        elif user is not None and user.role == "Admin":
            login(request,user)
            return redirect(views.adminindex)
        else:
            return HttpResponse("User does not exist")
      return render(request,'userapp/login.html')

def logoutview(request):
    logout(request)
    return redirect(loginview)

def menuview(request):
    return render(request,'userapp/menu.html')

def registerview(request):
     if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('password')
        password1 = request.POST.get('confirmpassword')
        if password == password1:
            try:
                User.objects.get(username=username)
                return HttpResponse("Username already exists")
            except:
                User.objects.create_user(username=username,
                                         password=password,
                                         email=email,
                                         phone=phone,
                                         address=address,)
                                        #  role ='Chef' ,
                                        #  is_superuser = True,
                                        #  is_staff = True)
                return redirect(loginview)
        else:
            return HttpResponse("password not match")
     return render(request,'userapp/register.html')
