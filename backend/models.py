from django.db import models
from django.conf import settings


class User(models.Model):
    """
    User Model for storing user details in Database
    uuid: Unique ID of the user
    name: Name of the user
    age: Age of the user
    email: Email of the user
    password: Password of the user
    country: Country of the user
    city: City of the user
    role: Role of the user
    contact_no: Contact number of the user
    """

    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    dob = models.DateField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(choices=[
        ('student', 'Student'), ('instructor', 'Instructor'), ('admin', 'Admin')
    ], max_length=20)
    contact_no = models.IntegerField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'Name: {self.first_name + ' ' + self.last_name}  \nEmail: {self.email} \nRole: {self.role}'


class Course(models.Model):
    """
    Course Model for storing course details in Database
    uuid: Unique ID of the course
    name: Name of the course
    description: Description of the course
    instructor: Instructor of the course
    students: Students enrolled in the course
    """

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instructor')
    students = models.ManyToManyField(User, related_name='students')

    def __str__(self):
        return f'Course Name: {self.name} \nInstructor: {self.instructor.first_name + ' ' + self.instructor.last_name}'
    

"""
Models for the LMS application.

This module contains the models for handling assessments and their submissions.

Classes:
    AssessmentModel
    AssessmentSubmission
"""





class Assessment(models.Model):
    """
    A model to represent an assessment.

    Attributes
    ----------
    title : str
        The title of the assessment.
    description : str
        A description of the assessment.
    deadline : datetime
        The deadline for the assessment.
    course : Course
        The course to which the assessment belongs.
    questions : File
        The file containing the assessment questions.
    submissions : ManyToManyField
        The student submissions related to this assessment.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    questions = models.FileField(upload_to='assessments/questions/')
    submissions = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        through='AssessmentSubmission', 
        related_name='assessment_submissions'
    )


class AssessmentSubmission(models.Model):
    """
    A model to represent a student's assessment submission.

    Attributes
    ----------
    assessment : ForeignKey
        The assessment being submitted.
    student : ForeignKey
        The student submitting the assessment.
    submission_file : File
        The file containing the student's submission.
    submitted_at : datetime
        The date and time the submission was made.
    """
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    submission_file = models.FileField(upload_to='assessments/submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)
