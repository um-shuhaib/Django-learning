from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
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