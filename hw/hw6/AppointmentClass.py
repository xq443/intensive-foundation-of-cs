# AppointmentClass.py
# Name: Xujia Qin
# Email: qin.xuj@northeastern.edu
# Date: Dec 8th, 2023
from DateClass import *
from TimeClass import *

class Appointment:
    """A class representing an appointment.

    Attributes:
        date (str): The date of the appointment.
        start_time (str): The starting time of the appointment.
        end_time (str): The ending time of the appointment.
        purpose (str): The purpose or description of the appointment.
    """
    def __init__(self, date, start_time, end_time, purpose):
        """
        Initializes an appointment with the provided details.

        Args:
            date (str): The date of the appointment.
            start_time (str): The starting time of the appointment.
            end_time (str): The ending time of the appointment.
            purpose (str): The purpose or description of the appointment.
        """
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.purpose = purpose

    def __str__(self):
        """
        Returns a string representation of the appointment.

        Returns:
            str: A string containing details of the appointment.
        """
        return "Date: " + str(self.date) + ", Time: " + str(self.start_time) + " to " + str(self.end_time) + ", Purpose: " + self.purpose
