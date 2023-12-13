# UserClass.py
# Name: Xujia Qin
# Email: qin.xuj@northeastern.edu
# Date: Dec 8th, 2023

from AppointmentDiaryClass import *

class User:
    """A class representing a user with an appointment diary.

    Attributes:
        username (str): The username of the user.
        appointment_diary (AppointmentDiary): An instance of the AppointmentDiary for managing appointments.
    """
    def __init__(self, username):
        """
        Initializes a user with a username and an empty appointment diary.

        Args:
            username (str): The username of the user.
        """
        self.username = username
        self.appointment_diary = AppointmentDiary()

    def get_username(self):
        """
        Retrieves the username of the user.

        Returns:
            str: The username of the user.
        """
        return self.username

    def get_appointment_diary(self):
        """
        Retrieves the appointment diary of the user.

        Returns:
            AppointmentDiary: The appointment diary instance associated with the user.
        """
        return self.appointment_diary
