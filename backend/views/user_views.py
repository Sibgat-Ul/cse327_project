from django.shortcuts import render, redirect
from backend.models import User, Course
from backend.forms import UserForm


def view_user_list(request):
    """
    View user list
    :param request:
    :return
    """
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'backend/users/user_list.html', context)

def login_user(request):
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
    return render(request, 'backend/users/user_login.html')

def register_user(request):
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