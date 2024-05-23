from backend.all_class.user_class.student import Student
from  backend.all_class.course_class  import Course
from .assessment import Assessment
from datetime import datetime

class AssessmentSubmission:
    """
    A class to represent a student's assessment submission.

    Attributes
    ----------
    submissionId : str
        The ID of the submission.
    submissionDateTime : datetime
        The date and time of the submission.
    submittedBy : Student
        The student who submitted the assessment.
    assessment : Assessment
        The assessment related to the submission.
    course : Course
        The course related to the submission.
    submittedFile : str
        The file path or name of the PDF file containing the student's submission.
    """
    def __init__(self, submissionId, submissionDateTime, submittedBy, assessment, course, submittedFile):
        self.submissionId = submissionId
        self.submissionDateTime = submissionDateTime
        self.submittedBy = submittedBy
        self.assessment = assessment
        self.course = course
        self.submittedFile = submittedFile

    def submit_assessment(self):
        """
        Submit the assessment.

        This method simulates the submission process by printing a message.

        Returns
        -------
        str
            A message confirming the submission.
        """
        submission_message = f"Assessment submission {self.submissionId} by {self.submittedBy} submitted successfully."
        print(submission_message)
        return submission_message
