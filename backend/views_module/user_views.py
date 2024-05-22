from django.shortcuts import render, redirect
from backend.models import User, Course
from backend.forms import  LoginForm, RegisterForm


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
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_users')
        
    context = {
        'form': form
    }
    return render(request, 'backend/users/register.html', context)


def student_view(request, id):
    """
    View student details

    :param request: Request type
    :param id: Student's ID
    :return:
    """
    courses = Course.objects.filter(students=id)

    context = {
        'courses': courses
    }
    return render(request, 'backend/users/student_view.html', context)


def instructor_view(request, id):
    """
    View instructor details

    :param request:
    :param id:
    :return:
    """
    instructor = User.objects.get(id=id, role='instructor')
    context = {
        'instructor': instructor
    }
    return render(request, 'backend/users/instructor_view.html', context)

def logout(request):
    """
    Logout user
    :param request:
    :return:
    """
    return redirect('home')
