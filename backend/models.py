from django.db import models


class User(models.Model):
    """
    User Model for storing user details in Database
    id: Unique ID of the user
    name: Name of the user
    age: Age of the user
    email: Email of the user
    password: Password of the user
    country: Country of the user
    city: City of the user
    role: Role of the user
    contact_no: Contact number of the user
    """

    id = models.BigAutoField(primary_key=True, default=0)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
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
    id: Unique ID of the course
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
    

class CourseMaterial(models.Model):
    """
    Model representing course materials.

    Attributes:
        course (Course): The course this material is associated with.
        title (str): The title of the course material.
        material_type (str): The type of the course material (document, video, link).
        content (str): The content or description of the course material.
        upload (FileField): The file uploaded for the course material.
    """
    MATERIAL_TYPE_CHOICES = [
        ('document', 'Document'),
        ('video', 'Video'),
        ('link', 'Link'),
    ]

    course = models.ForeignKey(Course, related_name='materials', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    material_type = models.CharField(max_length=10, choices=MATERIAL_TYPE_CHOICES)
    content = models.TextField()
    upload = models.FileField(upload_to='course_materials/', blank=True, null=True)

    def __str__(self):
        """
        Returns the string representation of the course material.

        Returns:
            str: The title of the course material.
        """
        return self.title    


class Announcement(models.Model):
    """
    Announcement Model for storing course details in Database

    Attributes:
        title (str): The title of the announcement.
        description (str): The description of the announcement.
        date (date): The date when the announcement was created.
        course (Course): The course to which the announcement belongs.
        created_by (User): The user who created the announcement.
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='announcements',
        help_text="The course to which the announcement belongs."
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_announcements',
        help_text="The user who created the announcement."
    )

    def __str__(self):
        """
        Returns the string representation of the announcement.

        Returns:
            str: The title of the announcement.
        """
        return self.title


 # Define the Event model to store event data in the database
class Event(models.Model):
    # Date field to store the date of the event
    date = models.DateField()
    # CharField to store the name of the event with a maximum length of 100 characters
    name = models.CharField(max_length=100)

    # String representation of the model to show the event name and date
    def __str__(self):
        return f"{self.name} on {self.date}"  
    
    
# Define the Student model with name and email fields
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
