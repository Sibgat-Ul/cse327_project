from django.shortcuts import render, redirect

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


from backend.views_module.announcement_views import (
    create_announcement,
    view_announcements
)