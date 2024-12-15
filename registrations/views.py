from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from . import forms


# Create your views here.
# @login_required(login_url="login_user")
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("/cadastros/register/")

    return render(request, "pages/login.html")


@login_required(login_url="/cadastros/")
def register_user(request):
    if request.method == "POST":
        form = forms.UserCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect("register_user")
    form = forms.UserCreate()
    return render(request, "pages/create_user.html", {"form": form})


@login_required(login_url="/cadastros/")
def logout_user(request):
    logout(request)
    messages.success(request, "Sistema encerrado! Até mais...")
    return redirect("login_user")


@login_required(login_url="/cadastros/")
def register_employee(request):
    if request.method == 'POST':
        form = forms.EmployeeCreate(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador registrado com sucesso!')
            return redirect("register_employee")
    form = forms.EmployeeCreate()
    return render(request, "pages/create_employee.html", {"form": form})
