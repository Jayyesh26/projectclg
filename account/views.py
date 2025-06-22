from logging import PlaceHolder
# import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from numpy import sign
from account.form import Signupform
from django.contrib import messages


def index(request):
    return render(request,"index.html")
def faculty(request):
    return render(request,"faculty.html")
def mba(request):   
    return render(request,"mba.html")
def bca(request):
    return render(request,"bca.html")
def bcom(request):
    return render(request,"bcom.html")
def bcomhr(request):
    return render(request,"bcomhr.html")
def bba(request):
    return render(request,"bba.html")
def eprakash(request):
    return render(request,"eprakash.html")
def pace(request):
    return render(request,"pace.html")
def gallery_(request):
    return render(request,"gallery.html")
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")
def sign_up(request):
    if request.method=="POST":
        fm = Signupform(request.POST)
        if fm.is_valid():
            use = fm.cleaned_data["username"]
            fn = fm.cleaned_data["first_name"]
            ln = fm.cleaned_data["last_name"]
            em = fm.cleaned_data["email"]
            pa1 = fm.cleaned_data["Password"]
            pa2 = fm.cleaned_data["Confirm_Password"]
            if pa1 != pa2:
                messages.add_message(request, messages.ERROR, 'Your password incorrect. ')
                return HttpResponse(request,"sign.html")
            reg = User.objects.create_user(username = use,email = em, password = pa1)
            reg.first_name=fn
            reg.last_name=ln
            reg.save()   
            messages.add_message(request, messages.SUCCESS, 'Your Account has been created !!!') 
            return HttpResponseRedirect("/sign/")
    else:
        fm = Signupform()
        messages.add_message(request, messages.SUCCESS, 'Your Account has been created !!!') 
        return render(request,"sign.html",{"data":fm})

def user_login(request):
    if request.method=="POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            user = fm.cleaned_data['username']
            passw = fm.cleaned_data['password']
            user=authenticate(username=user,password=passw)
            messages.info(request, 'You logged in') 
            if user is not None:
                login(request,user)
            return HttpResponseRedirect("/faculty/")   
    else:
        fm = AuthenticationForm()
        messages.error(request, 'You are invalid !') 
        return render(request,"login.html",{"form":fm})
        # return HttpResponseRedirect("/login/",{"form":fm})
    
# def faculty(request):
#     return render(request, 'template/faculty.html')
def contact(request):
    return render(request,"contact.html")
def Institute(request):
    return render(request,"Institute.html")
def international(request):
    return render(request,"international.html")
def welcome(request):
    return render(request,"welcome.html")