from django.forms import Form, CharField, ChoiceField, RadioSelect, IntegerField, DateField, ModelForm
from .models import User, Course ,Announcement


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class LoginForm(Form):
    username = CharField(max_length=100)
    password = CharField(max_length=100)
    role = CharField(max_length=10,
        widget=RadioSelect(
            choices=(
                ('admin', 'Admin'),
                ('student', 'Student'),
                ('teacher', 'Teacher')
            ),
            attrs={'class': 'form-check-input'}
        )
    )



class RegisterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First Name', 'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', 'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password', 'class': 'form-control'})
        self.fields['role'].widget.attrs.update({'class': 'form-control'})
        self.fields['dob'].widget.attrs.update({'class': 'form-control', 'placeholder': 'YYYY-MM-DD'})
        self.fields['contact_no'].widget.attrs.update({'placeholder': 'contact_no', 'class': 'form-control'})
        self.fields['country'].widget.attrs.update({'placeholder': 'Country', 'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'placeholder': 'City', 'class': 'form-control'})

    class Meta:
        model = User
        fields = '__all__'

class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'description', 'course']