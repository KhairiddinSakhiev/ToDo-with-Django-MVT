from django.shortcuts import render, HttpResponse, redirect
from .models import CustomUser as User
from django.contrib.auth import login, logout, authenticate


def register_view(request):
    if request.method == "GET":
        return render(request, 'auth/register.html')
    elif request.method == "POST":
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        confirm_password = request.POST.get('confirm_password', False)
        if not email or not password or not confirm_password:
            return HttpResponse('Pleas fill all inputs')
        if not password == confirm_password:
            return render(request, 'auth/register.html')
        user = User.objects.filter(email=email).exists()
        if user:
            return HttpResponse("User already exists")
        new_user = User.objects.create_user(
            email=email,
            password=password
        )
        
        return redirect('login')
    

def login_view(request):
    if request.method == "GET":
        return render(request, "auth/login.html")
    elif request.method=="POST":
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        if not username  or not password:
            return render(request, 'auth/login.html')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("task_list")
        return render(request, 'auth/login.html', 
                          {"username":username,
                           "error": "Invalid credentials"})
    

def logout_view(request):
    try:
        logout(request)
        return redirect("login")
    except Exception as ex:
        return HttpResponse(str(ex))    


