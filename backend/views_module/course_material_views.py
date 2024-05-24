from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse, Http404
from backend.models import Course, CourseMaterial
from backend.forms import CourseMaterialForm



def add_material(request, course_pk):
    """
    View to add new material to a course.

    Args:
        request (HttpRequest): The request object.
        course_pk (int): The primary key of the course.

    Returns:
        HttpResponse: The response with the form to add a new material.
    """
    course = get_object_or_404(Course, pk=course_pk)
    if request.method == 'POST':
        form = CourseMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.course = course
            material.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseMaterialForm()
    return render(request, 'add_material.html', {'form': form, 'course': course})

def delete_material(request, pk):
    """
    View to delete a specific course material.

    Args:
        request (HttpRequest): The request object.
        pk (int): The primary key of the course material.

    Returns:
        HttpResponse: The response redirecting to the course details.
    """
    material = get_object_or_404(CourseMaterial, pk=pk)
    course_pk = material.course.pk
    material.delete()
    return redirect('course_detail', pk=course_pk)

def download_material(request, pk):
    """
    View to download a specific course material.

    Args:
        request (HttpRequest): The request object.
        pk (int): The primary key of the course material.

    Returns:
        HttpResponse: The file response to download the material.
    """
    material = get_object_or_404(CourseMaterial, pk=pk)
    if not material.upload:
        raise Http404("No file uploaded for this material.")
    return FileResponse(material.upload.open(), as_attachment=True, filename=material.upload.name)