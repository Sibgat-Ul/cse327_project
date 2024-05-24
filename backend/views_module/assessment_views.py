from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from backend.models import Assignment, Submission, Course
from backend.forms import AssignmentForm, SubmissionForm, MarksForm

@login_required
def create_assessment(request, course_id):
    """
    Create a new assessment for a course.
    
    :param request: HTTP request object
    :param course_id: ID of the course
    :return: Rendered template for creating assessment
    """
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.course = course
            assignment.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = AssignmentForm()
    
    context = {
        'title': 'Create Assessment',
        'description': 'Create a new assessment for the course.',
        'form': form
    }
    return render(request, 'create_assessment.html', context)


@login_required
def view_assessment(request, assignment_id):
    """
    View the details of an assessment, including submissions.
    
    :param request: HTTP request object
    :param assignment_id: ID of the assignment
    :return: Rendered template for viewing assessment details
    """
    assignment = get_object_or_404(Assignment, id=assignment_id)
    submissions = assignment.submissions.all()
    
    context = {
        'title': assignment.title,
        'description': assignment.description,
        'assignment': assignment,
        'submissions': submissions
    }
    return render(request, 'view_assessment.html', context)


@login_required
def submit_assessment(request, assignment_id):
    """
    Submit an assignment.
    
    :param request: HTTP request object
    :param assignment_id: ID of the assignment
    :return: Rendered template for submitting assessment
    """
    assignment = get_object_or_404(Assignment, id=assignment_id)
    submission = Submission.objects.filter(student=request.user, assignment=assignment).first()
    
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES, instance=submission)
        if form.is_valid():
            new_submission = form.save(commit=False)
            new_submission.assignment = assignment
            new_submission.student = request.user
            new_submission.save()
            return redirect('view_assessment', assignment_id=assignment.id)
    else:
        form = SubmissionForm(instance=submission)
    
    context = {
        'title': f'Submit Assessment: {assignment.title}',
        'description': assignment.description,
        'form': form,
        'assignment': assignment
    }
    return render(request, 'submit_assessment.html', context)


@login_required
def view_submission(request, submission_id):
    """
    View the details of a student's submission.
    
    :param request: HTTP request object
    :param submission_id: ID of the submission
    :return: Rendered template for viewing submission details
    """
    submission = get_object_or_404(Submission, id=submission_id)
    
    context = {
        'title': f'Submission by {submission.student.username}',
        'description': f'Submitted on: {submission.submission_date}',
        'submission': submission
    }
    return render(request, 'view_submission.html', context)


@login_required
def assign_marks(request, submission_id):
    """
    Assign marks to a student's submission.
    
    :param request: HTTP request object
    :param submission_id: ID of the submission
    :return: Rendered template for assigning marks
    """
    submission = get_object_or_404(Submission, id=submission_id)
    
    if request.method == 'POST':
        form = MarksForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('view_assessment', assignment_id=submission.assignment.id)
    else:
        form = MarksForm(instance=submission)
    
    context = {
        'title': f'Assign Marks for {submission.student.username}\'s Submission',
        'description': f'Marks for the assignment: {submission.assignment.title}',
        'form': form,
        'submission': submission
    }
    return render(request, 'assign_marks.html', context)


@login_required
def view_marks(request):
    """
    View the marks for the logged-in student's submissions.
    
    :param request: HTTP request object
    :return: Rendered template displaying the student's marks
    """
    submissions = Submission.objects.filter(student=request.user)
    context = {
        'title': 'Your Marks',
        'submissions': submissions,
    }
    return render(request, 'view_marks.html', context)

