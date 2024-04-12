from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pass1 = request.POST['pass']

        user = authenticate(request,username=uname,password=pass1)

        if user is not None:
            auth_login(request,user)
            if user.is_superuser:
                messages.success(request, 'Login Success!')
                return redirect('dashboard')
            else:
                messages.success(request, 'Login Success!')
                return redirect('index')
        else:
            messages.error(request, 'Please Register!')
            return redirect("signup")

    return render(request, 'user/login.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password!=password2:
            messages.success(request, 'Password and Confirm Password Are not Match!')
            return redirect("signup")
        else:
            my_user = User.objects.create_user(uname,email,password)
            my_user.save()
            messages.success(request, 'Registration Success! Now You can Login!')
            return redirect('login')

    return render(request, 'user/signup.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

def update_profile(request):
    if request.method == "POST":
        user = request.user

        user.username = request.POST.get('username')
        user.email = request.POST.get('email')

        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('User_Dashboard')  # Assuming you have a 'profile' view defined
        

    return redirect('User_Dashboard')