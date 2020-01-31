from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def create_new_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/register")
    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        alias = request.POST['username'],
        email = request.POST['email'],
        password = pw_hash)
    messages.info(request, "Registration complete! You can log in now")
    return redirect("/")

def login(request):
    try:
        user = User.objects.get(email=request.POST['email'])
    except:
        messages.error(request, "Invalid email or password")
        return redirect("/")
    if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        messages.error(request, "Invalid email or password")
        return redirect("/")
    else:
        request.session['user_id'] = user.id
        request.session['username'] = user.alias
        return redirect("typingmaster/")