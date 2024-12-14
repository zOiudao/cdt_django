from django.shortcuts import render, redirect
from . import forms


# Create your views here.
def login_user(request):
    return render(request, "pages/login.html")


def register_user(request):
    if request.method == "POST":
        form = forms.UserCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_user")
        else:
            ...
    form = forms.UserCreate()
    return render(request, "pages/create_user.html", {"form": form})
