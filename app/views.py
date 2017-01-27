from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="login/")
def home(request):
	return render(request,"index.html")
@login_required(login_url="login/")
def charts(request):
	return render(request,"charts.html")
@login_required(login_url="login/")
def tables(request):
	return render(request,"tables.html")
@login_required(login_url="login/")
def widgets(request):
	return render(request,"widgets.html")
@login_required(login_url="login/")
def panels(request):
	return render(request,"panels.html")
