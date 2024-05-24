from django.urls import path

from . import views

urlpatterns = [
    # Handle users
    path('', views.home, name='home'),
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


