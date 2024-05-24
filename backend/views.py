from django.shortcuts import render, redirect
from .models import Event
from django.http import JsonResponse

from backend.views_module.assessment_views import(create_assessment,view_assessment,submit_assessment,view_submission,assign_marks,view_marks)
# Import course related views from course_views.py
from backend.views_module.course_views import (
    view_course_list,
    add_course,
    edit_course,
    delete_course,
    enroll,
    course_details
)

# Import user related views from user_views.py
from backend.views_module.user_views import (
    login,
    register,
    logout,
    student_view,
    instructor_view
)



# Define a view to render the calendar template
def calendar_view(request):
    return render(request, 'calendar_app/index.html')

# Define a view to fetch events from the database and return them as JSON
def get_events(request):
    events = Event.objects.all()
    event_list = [{"date": event.date.strftime("%Y-%m-%d"), "name": event.name} for event in events]
    return JsonResponse(event_list, safe=False)
