from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['Username']
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        password=request.POST['Password']
        cpassword=request.POST['Password1']
        if password==cpassword :
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username exists")
                return redirect('credential:register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=f_name,last_name=l_name)
                user.save();
                return redirect('credential:signin')

        else:
            messages.info(request,"Password doesn't match")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def signin(request):
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['Password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('bankapp:subscription')
        else:
            messages.info(request,"Invalid details")
            return redirect('credential:signin')
    return render(request,"login.html")
# Logout
def signout(request):
    auth.logout(request)
    return redirect('/')