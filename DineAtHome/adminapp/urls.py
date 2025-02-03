
from django.contrib import admin 
from django.urls import path 
from adminapp import views



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('adminindex/',views.adminindex,name="adminindex"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('usersprofileview/',views.usersprofileview,name="usersprofileview"),
    path('manageclientview/',views.manageclientview,name="manageclientview"),
    path('managechefview/',views.managechefview,name="managechefview"),
    path('manageorderview/',views.manageorderview,name="manageorderview"),
    path('formsvalidationview/',views.formsvalidationview,name="formsvalidationview"),
    path('tablesdataview/',views.tablesdataview,name="tablesdataview"),
    path('logoutview/',views.logoutview,name="logoutview"),
    path('tablesgeneralview/',views.tablesgeneralview,name="tablesgeneralview"),
    path('managefeedbackview/', views.managefeedbackview, name='managefeedbackview'),
    path('managefoodview/', views.managefoodview, name='managefoodview'),
]




    

