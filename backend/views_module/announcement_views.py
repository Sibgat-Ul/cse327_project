from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from backend.models import Course
from  backend.models import Announcement
from backend.forms import AnnouncementForm


@login_required

def create_announcement(request, course_id):
    """
    Create a new announcement for a course.

    Parameters:
        request (HttpRequest): The HTTP request object.
        course_id (int): The ID of the course for which the announcement is being created.

    Returns:
        HttpResponse: The HTTP response object.
    """
    # Retrieve the course object
    course = get_object_or_404(Course, id=course_id)
    
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.course = course
            announcement.created_by = request.user
            announcement.save()
            return redirect('view_announcements', course_id=course.id)
    else:
        form = AnnouncementForm()
    
    return render(request, 'create_announcement.html', {'form': form, 'course': course})

@login_required
def view_announcements(request, course_id):
    """
    View all announcements for a course.

    Parameters:
        request (HttpRequest): The HTTP request object.
        course_id (int): The ID of the course for which announcements are being viewed.

    Returns:
        HttpResponse: The HTTP response object.
    """
    # Retrieve the course object
    course = get_object_or_404(Course, id=course_id)
    # Retrieve all announcements for the course
    announcements = course.announcements.all().order_by('-date')
    
    return render(request, 'view_announcements.html', {'course': course, 'announcements': announcements})