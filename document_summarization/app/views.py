from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')   # email as username
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password != cpassword:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists!")
            return redirect("register")

        # Create Django User
        user = User.objects.create_user(username=username, password=password,
                                        first_name=fname, last_name=lname, email=username)


        messages.success(request, "Registration Successfully.")
        return redirect("log_in")

    return render(request, "register.html")

def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect("log_in")

    return render(request, "log_in.html")



def dashboard(request):
    if request.method == 'POST' and request.FILES.get('lname'):
        file = request.FILES['lname']
        UploadedFiles.objects.create(user=request.user, file=file)
        messages.success(request, "Document uploaded successfully!")
        return redirect('dashboard')  # or show success message

    return render(request, "dashboard.html")

def log_out(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("/")
