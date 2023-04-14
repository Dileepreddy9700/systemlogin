from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from LoginApp.models import Student, City, Course


# Create your views here.
def home(request):
    return render(request,'home.html')


def login_fun(request):
    return render(request,'login.html')


def register_fun(request):
    return render(request,'register.html')


def read_register(request):
    uname=request.POST['tbuname']
    email=request.POST['tbemail']
    password=request.POST['tbpass']
    user=User.objects.create_superuser(username=uname,email=email,password=password)
    user.save()
    return render(request,'login.html',{'msg':f'user created successfully user name is {uname}'})


def read_login(request):
    uname=request.POST['tbuname']
    password=request.POST['tbpass']
    user=authenticate(username=uname,password=password)
    if user is not None:
        login(request,user)
        b = Student.objects.all()
        return render(request,'index.html',{'data': b})
    else:
        return render(request,'login.html')


def logout_fun(request):
    logout(request)
    return redirect('login')

def addstudent(request):
    cities=City.objects.all()
    course=Course.objects.all()
    return render(request,'addstudent.html',{'cities':cities,'course':course})


def readstudentdata(request):
    s = Student()
    s.fname = request.POST['tbfname']
    s.lname = request.POST['tblname']
    s.mobile = request.POST['tbmob']
    s.email = request.POST['tbemail']
    s.CityName = City.objects.get(CityName=request.POST['ddlcity'])
    s.CourseName = Course.objects.get(CourseName=request.POST['ddlcourse'])
    s.save()
    return redirect('displaystudents')

def displaystudents(request):
    students = Student.objects.all()
    return render(request, 'displaystudents.html', {'data': students})


def updatestudent(request,id):
    cities = City.objects.all()
    course = Course.objects.all()
    s = Student.objects.get(id=id)
    if request.method == 'POST':
        s.fname = request.POST['tbfname']
        s.lname = request.POST['tblname']
        s.mobile = request.POST['tbmob']
        s.email = request.POST['tbemail']
        s.CityName = City.objects.get(CityName=request.POST['ddlcity'])
        s.CourseName = Course.objects.get(CourseName=request.POST['ddlcourse'])
        s.save()
        return redirect('displaystudents')
    return render(request,'updatestudent.html',{'data':s,'cities':cities,'course':course})


def deletestudent(request,id):
    s = Student.objects.get(id=id)
    s.delete()
    return redirect('displaystudents')
