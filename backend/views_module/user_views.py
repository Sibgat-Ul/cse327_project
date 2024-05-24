from django.shortcuts import render, redirect
from backend.models import User, Course
from backend.forms import LoginForm, RegisterForm


def login(request):
    """
    Login user

    :param request:
    :return:
    """
    loginForm = LoginForm(request.POST)

    if request.method == 'POST':
        if loginForm.is_valid():
            email = loginForm.cleaned_data.get('email')
            password = loginForm.cleaned_data.get('password')
            role = loginForm.cleaned_data.get('role')
            print(email, password, role)
            user = User.objects.filter(email=email, password=password, role=role).first()
            print(user)
            if user:
                return redirect(f'{role}/{user.id}/view')
            else:
                loginForm.add_error(None, 'Invalid credentials')

    return render(request, 'backend/users/login.html', context={'form': loginForm})


def register(request):
    """
    Register user

    :param request:
    :return:
    """
    form = RegisterForm(request.POST)

    context = {
        'form': form
    }

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            role = form.cleaned_data.get('role')
            form.save()
            id = User.objects.get(email=email)
            id = id.id
            print(email, password, role)
            return redirect(f'{role}/{id}/view')
        
    return render(request, 'backend/users/register.html', context)


def student_view(request, id):
    """
    View student details

    :param request: Request type
    :param id: Student's ID
    :return:
    """
    courses = Course.objects.filter(students=id)
    user = User.objects.get(id=id)

    context = {
        'courses': courses,
        'user': user
    }
    return render(request, 'backend/users/student_view.html', context)


def instructor_view(request, id):
    """
    View instructor details

    :param request:
    :param id:
    :return:
    """
    courses = Course.objects.filter(instructor=id)
    instructor = User.objects.get(id=id, role='instructor')
    context = {
        'user': instructor,
        'courses': courses
    }
    return render(request, 'backend/users/instructor_view.html', context)


def logout(request):
    """
    Logout user
    :param request:
    :return:
    """

    return redirect('login')
