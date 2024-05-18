from django.forms import Form, CharField, IntegerField, DateField, ModelForm
from .models import User, Course


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'