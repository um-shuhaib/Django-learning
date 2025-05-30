from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlog,logout as authlogout

# Create your views here.
def logout(request):
    authlogout(request)
    return redirect('login')
    





def login(request):
    error_msg=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            authlog(request,user)
            return redirect('list')
        else:
            error_msg='invalid credentials'


    return render(request,'users/login.html',{'error_msg':error_msg})


def signup(request):
    user=None
    error_msg=None
    if request.POST:
        
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        try:
            user=User.objects.create_user(password=password,username=username)
        except Exception as e:
            error_msg=str(e)

    return render(request,'users/signup.html',{'user':user,'error_msg':error_msg})