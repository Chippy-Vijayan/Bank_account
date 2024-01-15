from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from .models import register,branches
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(request):
    return render(request,'index.html')
def addbranches(request):
    if request.method == 'POST':
        name = request.POST['branch_name']
        url = request.POST['url_name']
        sub_branch = request.POST['sub_branch']
        add = branches(name=name,link=url,sub_branc=sub_branch)
        add.save()
        return redirect('bankapp:index')
    return render(request,'branches.html')
def subscription(request):
    if request.method=='POST':
        return redirect('bankapp:index')
    return render(request,'Subscription.html')
