# TimeClass.py
# Name: Xujia Qin
# Email: qin.xuj@northeastern.edu
# Date: Dec 8th, 2023
class Time:
    """A class representing a time.

    Attributes:
        hours (int): The hour part of the time.
        minutes (int): The minute part of the time.
        period (str): The period of the time (AM or PM).
    """
    def __init__(self, hours, minutes, period):
        """
        Initializes a time with the provided details.

        Args:
            hours (int): The hour part of the time.
            minutes (int): The minute part of the time.
            period (str): The period of the time (AM or PM).
        """
        self.hours = hours
        self.minutes = minutes
        self.period = period.upper()  # Ensure period is uppercase for comparison
        
    def __str__(self):
        """
        Returns a formatted string representation of the time.

        Returns:
            str: A string containing the formatted time in "HH:MM Period" format.
        """
        # Format hours and minutes with leading zeros if needed
        formatted_hours = str(self.hours).zfill(2)
        formatted_minutes = str(self.minutes).zfill(2)

        return formatted_hours + ":" + formatted_minutes + " " + self.period

    def to_minutes(self):
        """
        Converts the time to total minutes.

        Returns:
            int: Total minutes represented by the time.
        """
        total_minutes = self.hours * 60 + self.minutes
        if self.period == 'PM' and self.hours != 12:  # Exclude 12 PM for standard time calculation
            total_minutes += 12 * 60  # Add 12 hours if PM
        return total_minutes
    
    # Comparison methods for Time objects
    def __lt__(self, other):
        return self.to_minutes() < other.to_minutes()

    def __le__(self, other):
        return self.to_minutes() <= other.to_minutes()

    def __gt__(self, other):
        return self.to_minutes() > other.to_minutes()

    def __ge__(self, other):
        return self.to_minutes() >= other.to_minutes()

    def __eq__(self, other):
        return self.to_minutes() == other.to_minutes()

    def __ne__(self, other):
        return self.to_minutes() != other.to_minutes()
