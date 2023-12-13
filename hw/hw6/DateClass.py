# DateClass.py
# Name: Xujia Qin
# Email: qin.xuj@northeastern.edu
# Date: Dec 8th, 2023
class Date:
    """A class representing a date.

    Attributes:
        year (int): The year part of the date.
        month (int): The month part of the date.
        day (int): The day part of the date.
    """
    def __init__(self, year, month, day):
        """
        Initializes a date with the provided details.

        Args:
            year (int): The year part of the date.
            month (int): The month part of the date.
            day (int): The day part of the date.
        """
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        """
        Returns a formatted string representation of the date.

        Returns:
            str: A string containing the formatted date in "YYYY-MM DD" format.
        """
        return str(self.year).zfill(4) + "-" + str(self.month).zfill(2) + " " + self.day