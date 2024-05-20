from backend.all_class.course_class import Course


class Assessment:
    """
    Represents an assessment that belongs to a course and contains a list of questions.
    """

    def __init__(self, title, description, deadline, course, file_path):
        """
        Represents an assessment that belongs to a course and contains a list of questions.

        :param title: The title of the assessment.
        :type title: str
        :param description: The description of the assessment.
        :type description: str
        :param deadline: The deadline of the assessment.
        :type deadline: datetime.date
        :param course: The course to which the assessment belongs.
        :type course: Course
        :param file_path: The path to the file containing questions (PDF, DOC, TXT).
        :type file_path: str
        """
        self.title = title
        self.description = description
        self.deadline = deadline
        self.course = course
        self.file_path = file_path
        self.status = None

    def getTitle(self):
        """
        Get the title of the assessment.

        :return: The title of the assessment.
        :rtype: str
        """
        return self.title

    def setTitle(self, title):
        """
        Set the title of the assessment.

        :param title: The new title for the assessment.
        :type title: str
        """
        self.title = title

    def getDescription(self):
        """
        Get the description of the assessment.

        :return: The description of the assessment.
        :rtype: str
        """
        return self.description

    def setDescription(self, description):
        """
        Set the description of the assessment.

        :param description: The new description for the assessment.
        :type description: str
        """
        self.description = description

    def getDeadline(self):
        """
        Get the deadline of the assessment.

        :return: The deadline of the assessment.
        :rtype: datetime.date
        """
        return self.deadline

    def setDeadline(self, deadline):
        """
        Set the deadline of the assessment.

        :param deadline: The new deadline for the assessment.
        :type deadline: datetime.date
        """
        self.deadline = deadline

    def getCourse(self):
        """
        Get the course to which the assessment belongs.

        :return: The course to which the assessment belongs.
        :rtype: Course
        """
        return self.course

    def setCourse(self, course):
        """
        Set the course to which the assessment belongs.

        :param course: The new course for the assessment.
        :type course: Course
        """
        self.course = course

    def getQuestions(self):
        """
        Get the list of questions associated with the assessment.

        :return: The list of questions associated with the assessment.
        :rtype: list[Question]
        """
        return self.questions

    def getStatus(self):
        """
        Get the status of the assessment.

        :return: The status of the assessment.
        :rtype: AssignmentStatus
        """
        return self.status

    def setStatus(self, status):
        """
        Set the status of the assessment.

        :param status: The new status for the assessment.
        :type status: AssignmentStatus
        """
        self.status = status
