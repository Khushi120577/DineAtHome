
from django.contrib import admin 
from django.urls import path 
from userapp import views

urlpatterns = [
    path('loginview/',views.loginview,name="loginview"),
    path('logoutview/',views.logoutview,name="logoutview"),
    path('registerview/',views.registerview,name="registerview"),
    
    
    path('',views.indexview,name="indexview"),
    path('aboutview/',views.aboutview,name="aboutview"),
    path('blogview/',views.blogview,name="blogview"),
    path('blogdetailview/',views.blogdetailview,name="blogdetailview"),
    path('bookingview/',views.bookingview, name="bookingview"),
    path('chefview/',views.chefview,name="chefview"),
    path('menuview/',views.menuview,name="menuview"),
    
]




    

