from django.urls import path

from . import views

urlpatterns = [
    # Handle users
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),

    # Handle courses
    path('courses', views.view_course_list, name='courses'),
    path('courses/add_course', views.add_course, name='add_course'),
    path('courses/<int:id>/course_details', views.course_details, name='course_details'),
    path('courses/<int:id>/edit_course', views.edit_course, name='edit_course'),
    path('courses/<int:id>/delete_course', views.delete_course, name='delete_course'),
    path('courses/<int:id>/enroll', views.enroll, name='enroll'),

    # Handle Assessments
    path('create-assessment/<int:course_id>/', views.create_assessment, name='create_assessment'),
    path('view-assessment/<int:assignment_id>/', views.view_assessment, name='view_assessment'),
    path('submit-assessment/<int:assignment_id>/', views.submit_assessment, name='submit_assessment'),
    path('view-submission/<int:submission_id>/', views.view_submission, name='view_submission'),
    path('assign-marks/<int:submission_id>/', views.assign_marks, name='assign_marks'),
    path('view-marks/', views.view_marks, name='view_marks'),
]


    # Handle students
    path('student/<int:id>/view', views.student_view, name='student_view'),
    path('student/<int:id>/courses', views.view_course_list, name='view_course_list'),
    path('student/<int:id>/courses/enroll', views.enroll, name='enroll'),
    path('student/<int:id>/courses/<int:course_id>/details', views.course_details, name='course_details'),

    # Handle instructors
    path('instructor/<int:id>/view', views.instructor_view, name='instructor_view'),
    path('instructor/<int:id>/courses', views.view_course_list, name='view_course_list'),
    path('instructor/<int:id>/courses/<int:course_id>/details', views.course_details, name='course_details'),
    path('instructor/<int:id>/courses/add', views.add_course, name='add_course'),
    path('instructor/<int:id>/courses/<int:course_id>/edit', views.edit_course, name='edit_course'),
    path('instructor/<int:id>/courses/<int:course_id>/delete', views.delete_course, name='delete_course'),


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

