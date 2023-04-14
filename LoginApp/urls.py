from django.urls import path

from LoginApp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login_fun,name='login'),
    path('register',views.register_fun,name='register'),
    path('readregister',views.read_register,name='readregister'),
    path('readlogin',views.read_login,name='readlogin'),
    path('logout',views.logout_fun,name='logout'),
    path('addstudent', views.addstudent, name='addstudent'),
    path('readstudentdata', views.readstudentdata, name='readstudentdata'),
    path('displaystudents',views.displaystudents,name='displaystudents'),
    path('updatestudent/<int:id>',views.updatestudent,name='updatestudent'),
    path('deletestudent/<int:id>',views.deletestudent,name='deletestudent')
]