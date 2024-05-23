from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from backend.models import Assessment, AssessmentSubmission
from backend.forms import AssessmentForm, AssessmentSubmissionForm


@login_required
def create_assessment(request):
    """
    Handle the logic for creating an assessment.

    Parameters
    ----------
    request : HttpRequest
        The request object containing metadata about the request.

    Returns
    -------
    HttpResponse
        Rendered HTML response for creating an assessment.
    """
    if request.method == 'POST':
        form = AssessmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_assessment', assessment_id=form.instance.id)
    else:
        form = AssessmentForm()
    return render(request, 'assessments/create_assessment.html', {'form': form})


@login_required
def view_assessment(request, assessment_id):
    """
    Display the details of an assessment.

    Parameters
    ----------
    request : HttpRequest
        The request object containing metadata about the request.
    assessment_id : int
        The ID of the assessment to view.

    Returns
    -------
    HttpResponse
        Rendered HTML response displaying the assessment details.
    """
    assessment = get_object_or_404(Assessment, id=assessment_id)
    return render(request, 'assessments/view_assessment.html', {'assessment': assessment})


@login_required
def submit_assessment(request, assessment_id):
    """
    Handle the logic for submitting an assessment.

    Only accessible by students.

    Parameters
    ----------
    request : HttpRequest
        The request object containing metadata about the request.
    assessment_id : int
        The ID of the assessment to be submitted.

    Returns
    -------
    HttpResponse
        A response indicating the submission status.
    """
    if request.user.role != 'student':
        return HttpResponse('Unauthorized', status=401)

    assessment = get_object_or_404(Assessment, id=assessment_id)

    if request.method == 'POST':
        form = AssessmentSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.assessment = assessment
            submission.student = request.user
            submission.save()
            return HttpResponse("Assessment submitted successfully.")
    else:
        form = AssessmentSubmissionForm()

    return render(request, 'assessments/submit_assessment.html', {'form': form})

@login_required
def view_submission(request, submission_id):
    """
    Display the details of an assessment submission.

    Parameters
    ----------
    request : HttpRequest
        The request object containing metadata about the request
    submission_id : int
        The ID of the submission to view

    Returns
    -------
    HttpResponse
        Rendered HTML response displaying the submission details
    """
    submission = get_object_or_404(AssessmentSubmission, id=submission_id)
    return render(request, 'assessments/view_submission.html', {'submission': submission})