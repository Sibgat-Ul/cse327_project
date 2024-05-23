from django.forms import Form, CharField, ChoiceField, IntegerField, DateField, ModelForm
from .models import User, Course , Assessment , AssessmentSubmission
from django.utils import timezone


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
    role = ChoiceField(choices=(
            ('admin', 'Admin'),
            ('student', 'Student'),
            ('teacher', 'Teacher')
        ),
        required=True
    )


class RegisterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First Name', 'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', 'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password', 'class': 'form-control'})
        self.fields['role'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = '__all__'

class AssessmentForm(ModelForm):
    
    
    class Meta:
        model = Assessment
        fields = '__all__'

class AssessmentSubmissionForm(ModelForm):
    """
    Form for submitting an assessment.
    """
    class Meta:
        model = AssessmentSubmission
        fields = ['submittedFile']
        
    def __init__(self, *args, **kwargs):
        self.student = kwargs.pop('student', None)
        self.assessment = kwargs.pop('assessment', None)
        self.course = kwargs.pop('course', None)
        super().__init__(*args, **kwargs)
    
    def save(self, commit=True):
        submission = super().save(commit=False)
        submission.submittedBy = self.student
        submission.assessment = self.assessment
        submission.course = self.course
        submission.submissionDateTime = timezone.now()
        if commit:
            submission.save()
        return submission