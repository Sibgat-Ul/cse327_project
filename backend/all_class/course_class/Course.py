

class Course:
    """
    Course class to create course object
    """
    def __init__(
            self,
            course_id,
            course_name,
            course_description,
            course_credit,
            course_department,
            course_level,
            course_hour,
    ):
        """
        Course class to create course object

        :param course_id: Course ID
        :param course_name: Course Name
        :param course_description: Course Description
        :param course_credit: Course Credit
        :param course_department: Course Department
        :param course_level: Course Level
        :param course_hour: Course Hour
        """
        self.course_id = course_id
        self.course_name = course_name
        self.course_description = course_description
        self.course_credit = course_credit
        self.course_department = course_department
        self.course_level = course_level
        self.course_hour = course_hour

        self.announcements = []
        self.course_material = []
        self.course_assignment = []
        self.course_assessment = []

    def __str__(self):
        return (
            f"Course ID: {self.course_id}, "
            f"Course Name: {self.course_name}, "
            f"Course Description: {self.course_description}, "
            f"Course Credit: {self.course_credit}, "
            f"Course Department: {self.course_department}, "
            f"Course Level: {self.course_level}"
        )

    def add_announcement(self, announcement: str) -> None:
        """
        Add announcement to course

        :param announcement: Announcement
        :return: None
        """
        self.announcements.append(announcement)

    def get_announcements(self) -> list:
        """
        Get announcements of course

        :return: List of announcements
        """
        return self.announcements

    def add_course_material(self, course_material: str) -> None:
        """
        Add course material to course

        :param course_material: Course Material
        :return: None
        """
        self.course_material.append(course_material)

    def get_course_material(self) -> list:
        """
        Get course material of course

        :return: List of course material
        """
        return self.course_material

    def add_course_assignment(self, course_assignment: str) -> None:
        """
        Add course assignment to course

        :param course_assignment: Course Assignment
        :return: None
        """
        self.course_assignment.append(course_assignment)