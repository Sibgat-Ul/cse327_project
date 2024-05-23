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
    path('assessments/', views.AssessmentListView.as_view(), name='assessment_list'),
    path('assessments/<int:pk>/', views.AssessmentDetailView.as_view(), name='assessment_detail'),
    path('assessments/create/', views.AssessmentCreateView.as_view(), name='assessment_create'),
    
    # Handle Assessments
    path('assessments/<int:assessment_id>/submit/', views.submit_assessment, name='submit_assessment'),
    path('submission/<int:submission_id>/', views.view_submission, name='view_submission'),

]
