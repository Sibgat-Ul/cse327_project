import numpy as np


class User:
    """
    User class to store user details
    """

    def __init__(
            self,
            name: str,
            age: np.int16,
            email: str,
            password: str,
            country: str,
            city: str,
            role: str,
            contact_no: np.int16,
    ):
        """
        :param name: Name of the user
        :param age: Age of the user
        :param email: Email of the user
        :param password: Password of the user
        :param country: Country of the user
        :param city: City of the user
        :param role: Role of the user
        :param contact_no: Contact number of the user
        """
        self.username = name
        self.age = age
        self.email = email
        self.password = password
        self.country = country
        self.city = city
        self.role = role
        self.contact_no = contact_no

        self.courses = []

        self.user_id = None

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username

    def change_password(self, new_password: str) -> None:
        """
        Change password of the user
        :param new_password: New password
        :return: None
        """

        self.password = new_password

    def change_email(self, new_email: str) -> None:
        """
        Change email of the user
        :param new_email: New email
        :return: None
        """

        self.email = new_email

    def change_contact_no(self, new_contact_no: np.int16) -> None:
        """
        Change contact number of the user
        :param new_contact_no: New contact number
        :return: None
        """

        self.contact_no = new_contact_no

    def generate_user_id(self) -> None:
        """
        Generate user id using email
        :return: None
        """

        self.user_id = hash(self.email)

    def hash_password(self) -> None:
        """
        Hash the password using email
        :return:
        """

        self.password = hash(self.password + self.email)

    def get_user_details(self) -> dict:
        """
        Get user details

        :return: Dictionary of user details
        """

        return self.to_dict()

    def to_dict(self) -> dict:
        """
        Convert object to dictionary
        :return: Dictionary of user details
        """
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'role': self.role
        }
