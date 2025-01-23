from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def indexview(request):
    return render(request, 'userapp/index.html')

def aboutview(request):
    return render(request,'userapp/about.html')

def featureview(request):
    return render(request,'userapp/feature.html')

def menuview(request):
    return render(request,'userapp/menu.html')

def bookingview(request):
    return render(request,'userapp/booking.html')

def contactview(request):
    return render(request,'userapp/contact.html')

def chefview(request):
    return render(request,'userapp/chef.html')

def blogview(request):
    return render(request,'userapp/blog.html')

def blogdetailview(request):
    return render(request,'userapp/blogdetail.html')

def loginview(request):
        return render(request,'userapp/login.html')

def registerview(request):
        return render(request,'userapp/register.html')
