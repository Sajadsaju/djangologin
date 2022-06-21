from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from log.forms import CreateUserForm


def Home(request):
    if request.method=='POST':
        username=request.POST.get('user')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
    return render(request,'index.html')
def register(request):
    form=CreateUserForm
    context={'form':form}
    if request.method=='POST':
        form1=CreateUserForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('home')
    return render(request,'register.html',context)

@login_required(login_url='home')
def profile(request):
    return render(request,'profile.html')
    
    