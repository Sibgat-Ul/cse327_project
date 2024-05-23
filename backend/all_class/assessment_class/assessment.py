from backend.all_class.course_class import Course 
from .assessmentSubmission import AssessmentSubmission
from datetime import datetime
from django.core.files import File







class Assessment:
    """
    A class used to represent an Assessment.

    Attributes
    ----------
    title : str
        the title of the assessment
    description : str
        the description of the assessment
    deadline : datetime
        the deadline of the assessment
    course : Course
        the course to which the assessment belongs
    questions : File
        the questions file of the assessment

    Methods
    -------
    getTitle()
        Returns the title of the assessment.
    setTitle(title)
        Sets the title of the assessment.
    getDescription()
        Returns the description of the assessment.
    setDescription(description)
        Sets the description of the assessment.
    getDeadline()
        Returns the deadline of the assessment.
    setDeadline(deadline)
        Sets the deadline of the assessment.
    getCourse()
        Returns the course of the assessment.
    setCourse(course)
        Sets the course of the assessment.
    getQuestions()
        Returns the questions file of the assessment.
    setQuestions(questions)
        Sets the questions file of the assessment.
    createAssessment()
        Saves the assessment.
    viewAssessment()
        Returns the assessment instance.
    submitAssessment()
        Placeholder for assessment submission logic.
    """

    def __init__(self, title, description, deadline, course, questions):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.course = course
        self.questions = questions

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

    def getDeadline(self):
        return self.deadline

    def setDeadline(self, deadline):
        self.deadline = deadline

    def getCourse(self):
        return self.course

    def setCourse(self, course):
        self.course = course

    def getQuestions(self):
        return self.questions

    def setQuestions(self, questions):
        self.questions = questions

    def createAssessment(self):
        """
        Saves the assessment to the database.
        """
        assessment = Assessment(
            title=self.title,
            description=self.description,
            deadline=self.deadline,
            course=self.course,
            questions=self.questions
        )
        assessment.save()

    def viewAssessment(self, assessment_id):
        """
        Retrieves the assessment instance from the database.

        Parameters
        ----------
        assessment_id : int
            The ID of the assessment to retrieve.

        Returns
        -------
        AssessmentModel
            The assessment instance.
        """
        return Assessment.objects.get(id=assessment_id)

    def submitAssessment(self, assessment_id, student, submission_file):
        """
        Submits an assessment by saving the submission to the database.

        Parameters
        ----------
        assessment_id : int
            The ID of the assessment being submitted.
        student : User
            The student who is submitting the assessment.
        submission_file : File
            The file being submitted.

        Returns
        -------
        AssessmentSubmission
            The created assessment submission instance.
        """
        assessment = self.viewAssessment(assessment_id)
        submission = AssessmentSubmission(
            assessment=assessment,
            student=student,
            submission_file=submission_file
        )
        submission.save()
        return submission
