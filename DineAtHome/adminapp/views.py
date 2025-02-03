from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from adminapp import models
from django.contrib.auth.models import User

def adminindex(request):
    return render(request,'adminapp/index.html')



def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)

        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            print("auth")
            return redirect(adminindex)  # Redirect to home or a dashboard page
        else:
           print("error")
           return redirect(admin_login)
    return render(request, 'adminapp/pages-login.html')
    

def logoutview(request):
    logout(request)
    return redirect(admin_login)


def usersprofileview(request):
    return render(request,'adminapp/users-profile.html')

def managechefview(request):
    return render(request,'adminapp/manage_chef.html')

def manageclientview(request): 
    return render(request,'adminapp/manage_clients.html')


def tablesgeneralview(request):
    return render(request,'adminapp/tables-general.html')

def manageorderview(request):
    return render(request,'adminapp/manage_order.html')

def formsvalidationview(request):
    return render(request,'forms-validation.html')

def tablesdataview(request):
    return render(request,'adminapp/tables-data.html')

def managefeedbackview(request):
    return render(request,'adminapp/manage_feedback.html')

def managefoodview(request):
    return render(request,'adminapp/manage_food.html')