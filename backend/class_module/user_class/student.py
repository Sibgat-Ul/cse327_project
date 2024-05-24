from backend.class_module.user_class.users import User


class Student(User):
    """
    Student class to create student object
    """
    def __init__(self, name, age, email, country, city, password, contact_no):
        """
        Student class to create student object

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
            role='student',
            contact_no=contact_no
        )
        self.courses = []

    def enroll_course(self, course: dict) -> None:
        """
        Enroll student to a course

        :param course:
        :return:
        """
        self.courses.append(course)

    def get_courses(self) -> list:
        """
        Get courses of student

        :return:
        """
        return self.courses

    def get_student_details(self) -> dict:
        return self.get_user_details()
