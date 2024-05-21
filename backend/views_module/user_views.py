from django.shortcuts import render, redirect
from backend.models import User, Course
from backend.forms import UserForm, LoginForm


def login(request):
    """
    Login user

    :param request:
    :return:
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username, password=password)
        if user:
            return redirect('home')
    return render(request, 'backend/users/login.html', context={'form': LoginForm})


def register(request):
    """
    Register user

    :param request:
    :return:
    """
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_users')
        
    context = {
        'form': form
    }
    return render(request, 'backend/users/register.html', context)


def home(request):
    """
    Home page

    :param request:
    :return:
    """
    return render(request, 'backend/home.html')


def logout(request):
    """
    Logout user
    :param request:
    :return:
    """
    return redirect('home')
