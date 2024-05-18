from django.urls import path

from . import views

urlpatterns = [
    # Handle users
    path('', views.home, name='home'),
    path('/login', views.login, name='login'),
    path('/register', views.register, name='register'),
    path('/logout', views.logout, name='logout'),

    # Handle profile
    path('/profile', views.profile, name='profile'),
    path('/edit_profile', views.edit_profile, name='edit_profile'),
    path('/change_password', views.change_password, name='change_password'),
    path('/forgot_password', views.forgot_password, name='forgot_password'),

    # Handle courses
    path('/courses', views.courses, name='courses'),
    path('/courses/add_course', views.add_course, name='add_course'),
    path('/courses/<int:id>/course_details', views.course_details, name='course_details'),
    path('/courses/<int:id>/edit_course', views.edit_course, name='edit_course'),
    path('/courses/<int:id>/delete_course', views.delete_course, name='delete_course'),
    path('/courses/<int:id>/enroll', views.enroll, name='enroll'),
]
