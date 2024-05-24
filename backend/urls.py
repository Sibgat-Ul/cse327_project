from django.urls import path

from . import views

urlpatterns = [
    # Handle users
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),

    # Handle students
    path('students/<int:id>/view', views.student_view, name='students'),
    path('students/<int:id>/courses/enroll', views.enroll, name='enroll'),
    path('students/<int:id>/courses/<int:course_id>/details', views.course_details, name='course_details'),

    # Handle instructors
    path('instructors/<int:id>/view', views.instructor_view, name='instructors'),
    path('instructors/<int:id>/courses', views.view_course_list, name='view_course_list'),
    path('instructors/<int:id>/courses/<int:course_id>/details', views.course_details, name='course_details'),
    path('instructors/<int:id>/courses/add', views.add_course, name='add_course'),
    path('instructors/<int:id>/courses/<int:course_id>/edit', views.edit_course, name='edit_course'),
    path('instructors/<int:id>/courses/<int:course_id>/delete', views.delete_course, name='delete_course'),


    # Handle courses


    #Handle announcements
    path('course/<int:course_id>/create-announcement/', views.create_announcement, name='create_announcement'),
    path('course/<int:course_id>/announcements/', views.view_announcements, name='view_announcements'),

]


# Define URL patterns for the calendar view and event fetching API
urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('api/events/', views.get_events, name='get_events'),
]


# Define the URL pattern for the student list view
urlpatterns = [
    path('', views.student_list, name='student_list'),
]

