class Announcement:
    """
    A class to represent an announcement.

    Attributes:
        title (str): The title of the announcement.
        description (str): The description of the announcement.
        created_by (str): The user who created the announcement.
        created_at (str): The date and time when the announcement was created.
    """

    def __init__(self, title, description, created_by, created_at):
        """
        Initialize an Announcement object.

        :param title: Title of the announcement
        :type title: str
        :param description: Description of the announcement
        :type description: str
        :param created_by: User who created the announcement
        :type created_by: str
        :param created_at: Date and time when the announcement was created
        :type created_at: str
        """
        self.title = title
        self.description = description
        self.created_by = created_by
        self.created_at = created_at

    def __str__(self):
        """
        Return a string representation of the announcement.

        :return: String representation of the announcement
        :rtype: str
        """
        return self.title