from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Course,Department
from collage_app.forms import MyForm


# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,
                            password=password)

        if user is not None:
            auth_login(request, user)
            messages.info(request, "You are logged in")
            return redirect('tem')
        else:
            messages.info(request, "invalid username or password")
            return redirect('login')
    return render(request, 'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        print(email,username,password)

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "user name exist")
                return redirect('register')



            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist")
                return redirect('register')


            else:
                my_user=User.objects.create_user(username,email,password)
                my_user.save()

                messages.info(request, "user created")
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')

    return render(request, 'register.html')
def tem(request):
    return render(request,'but.html')
def index(request):
    return render(request,'index.html')
def logout(request):
    return render(request,'tem.html')




def form(request):

    if request.method=="POST":

       messages.info(request, "Your Reistration Succesfully Completed")
       return redirect('form')


    return render(request,'form.html',{'form':form})
def form1(request):
    return render(request,'form1.html')
