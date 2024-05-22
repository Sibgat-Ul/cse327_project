from backend.class_module.user_class.users import User
from backend.class_module.course_class import Course

class Instructor(User):
    """
    Instructor class to create instructor object
    """
    def __init__(self, name, age, email, country, city, password, contact_no):
        """
        Instructor class to create instructor object

        :param name:
        :param age:
        :param email:
        :param country:
        :param city:
        :param password:
        :param contact_no:
        """
        super().__init__(
            name=name,
            age=age,
            email=email,
            password=password,
            country=country,
            city=city,
            role='instructor',
            contact_no=contact_no
        )
        self.courses = []

    def create_course(self, course: dict) -> None:
        """
        Create course by instructor

        :param course:
        :return:
        """
        self.courses.append(course)

    def delete_course(self, course: dict) -> None:
        """
        Delete course by instructor

        :param course:
        :return:
        """
        self.courses.remove(course)

    def get_courses(self) -> list:
        """
        Get courses of instructor

        :return:
        """
        return self.courses

    def get_instructor_details(self) -> dict:
        return self.get_user_details()