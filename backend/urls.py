from django.urls import path

from . import views

urlpatterns = [
    # Handle users
    path('', views.home, name='home'),
    path('/login', views.login, name='login'),
    path('/register', views.register, name='register'),
    path('/logout', views.logout, name='logout'),

    # Handle courses
    path('/courses', views.view_course_list, name='courses'),
    path('/courses/add_course', views.add_course, name='add_course'),
    path('/courses/<int:id>/course_details', views.course_details, name='course_details'),
    path('/courses/<int:id>/edit_course', views.edit_course, name='edit_course'),
    path('/courses/<int:id>/delete_course', views.delete_course, name='delete_course'),
    path('/courses/<int:id>/enroll', views.enroll, name='enroll'),
]
