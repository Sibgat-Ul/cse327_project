from django.shortcuts import render, redirect
from backend.views.course_views import view_course_list, add_course, edit_course, delete_course
# Create your views here.
def home(request):
    return render(request, 'backend/home.html')

