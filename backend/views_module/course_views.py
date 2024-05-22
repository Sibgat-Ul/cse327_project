from django.shortcuts import render, redirect
from backend.models import User, Course


def view_course_list(request, id, role):
    """
    View courses list

    :param request:
    :return:
    """
    courses = Course.objects.get(instructor_id=id)
    context = {
        'courses': [courses]
    }
    return render(request, 'backend/courses/course_list.html', context)


def add_course(request):
    """
    Add course

    :param request:
    :return:
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        course = Course(name=name, description=description)
        course.save()
        return redirect('view_courses')
    return render(request, 'backend/courses/course_add.html')


def edit_course(request, id):
    """
    Edit course

    :param request:
    :param id:
    :return:
    """
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        course.name = request.POST.get('name')
        course.description = request.POST.get('description')
        course.save()
        return redirect('view_courses')
    context = {
        'course': course
    }
    return render(request, 'backend/courses/course_edit.html', context)


def delete_course(request, id):
    """
    Delete course

    :param request: Request type
    :param id: int
    :return:
    """
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('view_courses')


def course_details(request, id):
    """
    View course details

    :param request: request type
    :param id: int
    :return: render
    """
    course = Course.objects.get(id=id)
    context = {
        'course': course
    }
    return render(request, 'backend/courses/course_view.html', context)


def enroll(request, id):
    """
    Enroll in course

    :param request: request type
    :param id: int
    :return: redirect
    """
    course = Course.objects.get(id=id)
    user = User.objects.get(id=1)
    course.users.add(user)
    return redirect('view_courses')