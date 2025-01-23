from django.urls import path
from userapp import views

urlpatterns = [
    path('indexview/',views.indexview,name="indexview"),
    path('aboutview/',views.aboutview,name="aboutview"),
    path('featureview/',views.featureview,name="featureview"),
    path('menuview/',views.menuview,name="menuview"),
    path('bookingview/',views.bookingview,name="bookingview"),
    path('contactview/',views.contactview,name="contactview"),
    path('chefview/',views.chefview,name="chefview"),
    path('blogview/',views.blogview,name="blogview"),
    path('blogdetailview/',views.blogdetailview,name="blogdetailview"),
    path('registerview/',views.registerview,name="registerview"),
    path('loginview/',views.loginview,name="loginview"),
]
