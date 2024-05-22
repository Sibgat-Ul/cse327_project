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
    
    from django.db import models

class Announcement(models.Model):
    """
    Model representing an announcement for a course.

    Attributes:
        title (str): The title of the announcement.
        description (str): The description of the announcement.
        course (Course): The course related to the announcement.
        created_by (User): The user who created the announcement.
        created_at (datetime): The date and time when the announcement was created.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    created_by = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the announcement.

        Returns:
            str: The title of the announcement.
        """
        return self.title