from django.shortcuts import render, redirect
from backend.views_module.course_views import (
    view_course_list, add_course, edit_course, delete_course, enroll, course_details
)
from backend.views_module.user_views import (login, register, logout, home)

