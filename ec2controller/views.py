from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . import control

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'file.html')

def LoginPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=uname,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!")

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def start_instance(request):
    control.start_instance()
    return HttpResponse("Started")

@login_required(login_url='login')
def stop_instance(request):
    control.stop_instance()
    return HttpResponse("Stopped")
