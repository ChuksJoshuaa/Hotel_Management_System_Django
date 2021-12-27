import requests
from django.shortcuts import render, redirect
from .models import Customer, Manager
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import auth
from .forms import accountform


def user_login(request):
    if request.session.get('username', None) and request.session.get('type', None) == 'customer':
        return redirect('user_dashboard')
    if request.session.get('username', None) and request.session.get('type', None) == 'manager':
        return redirect('manager_dashboard')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if not len(username):
            messages.warning(request, "Username field is empty")
            return redirect('user_login')
        elif not len(password):
            messages.warning(request, "Password field is empty")
            return redirect('user_login')
        else:
            pass
        if Customer.objects.filter(username=username):
            if Customer.objects.filter(username=username):
                user = Customer.objects.filter(username=username)[0]
                password_hash = user.password
                res = check_password(password, password_hash)
                if res == 1:
                    request.session['username'] = username
                    request.session['type'] = 'customer'
                    return redirect('home')
                else:
                    user = Customer.objects.filter(password=password).exists()
                    password_hash = user
                    if res:
                       res = check_password(password, password_hash)
                    else:
                        messages.warning(request, "Password is incorrect")
                        return redirect('user_login')
                    if res == 1:
                        request.session['username'] = username
                        request.session['type'] = 'customer'
                        user = auth.authenticate(username=username, password=password)
                        auth.login(request, user)
                        return redirect('home')
                    else:
                        messages.warning(request, "Password is incorrect")
                        return redirect('user_login')
            else:
                messages.warning(request, "username does not exist")
                return redirect('user_login')
        else:
            messages.warning(request, "No account exist for the given Username")
            return redirect('user_login')
    else:
        redirect('user_login')
    return render(request, 'accounts/user_login.html', {})


def manager_login(request):
    if request.session.get('username', None) and request.session.get('type', None) == 'customer':
        return redirect('user_dashboard')
    if request.session.get('username', None) and request.session.get('type', None) == 'manager':
        return redirect('manager_dashboard')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if not len(username):
            messages.warning(request, "Username field is empty")
            return redirect('manager_login')
        elif not len(password):
            messages.warning(request, "Password field is empty")
            return redirect('manager_login')
        else:
            pass
        if Manager.objects.filter(username=username):
            user = Manager.objects.filter(username=username)[0]
            password_hash = user.password
            res = check_password(password, password_hash)
            if res:
                request.session['username'] = username
                request.session['type'] = 'manager'
                return redirect('home')
            else:
                user = Manager.objects.filter(password=password).exists()
                password_hash = user
                if res:
                    res = check_password(password, password_hash)
                else:
                    messages.warning(request, "Password is incorrect")
                    return redirect('manager_login')
                if res == 1:
                    request.session['username'] = username
                    request.session['type'] = 'manager'
                    user = auth.authenticate(username=username, password=password)
                    auth.login(request, user)
                    return redirect('home')
                else:
                    messages.warning(request, "Password is incorrect")
                    return redirect('manager_login')
        else:
            messages.warning(request, "No account exist for the given Username")
            return redirect('manager_login')
    else:
        redirect('manager_login')
    return render(request, 'accounts/manager_login.html', {})


def user_signup(request):
    form = accountform()
    if request.session.get('username', None) and request.session.get('type', None) == 'customer':
        return redirect('user_dashboard')
    if request.session.get('username', None) and request.session.get('type', None) == 'manager':
        return redirect('manager_dashboard')
    if request.method == "POST":
        form = accountform(request.POST)
        if form.is_valid():
            form.save()
        username = request.POST['username']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        image = request.FILES.get('image', None)
        password = request.POST['password']
        if username:
            if Customer.objects.filter(username=username).exists():
                messages.warning(request, "Account already exist, please login to continue")
                return redirect('user_login')
            else:
                password_hash = make_password(password)
                user = Customer(username=username, email=email, image=image, password=password_hash, phone_no=phone_no)
                user.save()
                messages.success(request, "Account Created Successfully, Please login to continue")
                return redirect('user_login')
        else:
            messages.warning(request, "Username does not exist.")
            return redirect('user_signup')
    else:
        form = accountform()
        return render(request, 'accounts/user_signup.html', {"form": form})


def manager_signup(request):
    form = accountform()
    if request.session.get('username', None) and request.session.get('type', None) == 'customer':
        return redirect('user_dashboard')
    if request.session.get('username', None) and request.session.get('type', None) == 'manager':
        return redirect('manager_dashboard')
    if request.method == "POST":
        form = accountform(request.POST)
        if form.is_valid():
            form.save()
        username = request.POST['username']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        image = request.FILES.get('image', None)
        password = request.POST['password']

        if username:
            if Manager.objects.filter(username=username).exists():
                messages.warning(request, "Account already exist, please login to continue")
                return redirect('manager_login')
            else:
                password_hash = make_password(password)
                user = Manager(username=username, email=email, image=image, password=password_hash, phone_no=phone_no)
                user.save()
                messages.success(request, "Account Created Successfully, Please login to continue")
                return redirect('manager_login')
        else:
            messages.warning(request, "Username does not exist.")
            return redirect('manager_signup')
    else:
        form = accountform()
        return render(request, 'accounts/manager_signup.html', {"form": form})


def logout(request):
    if request.session.get('username', None):
        del request.session['username']
        del request.session['type']
        return render(request, "accounts/user_logout.html", {})
    else:
        return render(request, "accounts/user_login.html", {})



