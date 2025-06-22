from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Signupform(forms.Form):
     username = forms.CharField(widget=forms.TextInput(attrs={"class":"usname cm","placeholder":"username"}))
     first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"Fname cm","placeholder":"First name"}))
     last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"Lname cm","placeholder":"Last name"}))
     email = forms.EmailField(widget=forms.TextInput(attrs={"class":"Email cm","placeholder":"Email"}))
     Password = forms.CharField(widget=forms.TextInput(attrs={"class":"Password cm","placeholder":"Password"}))
     Confirm_Password = forms.CharField(widget=forms.TextInput(attrs={"class":"Cpassword cm","placeholder":"Confirm Password","color":"black" }))