# AppointmentDiaryClass.py
# Name: Xujia Qin
# Email: qin.xuj@northeastern.edu
# Date: Dec 8th, 2023


class AppointmentDiary:
    """A class representing an appointment diary.

    Attributes:
        appointments (list): A list to store appointments.
    """
    def __init__(self):
        self.appointments = []

    def add_appointment(self, appointment):
        """Adds a new appointment to the diary.

        Args:
            appointment (str): The appointment to be added.
        """
        self.appointments.append(appointment)

    def remove_appointment(self, appointment):
        """Removes a specific appointment from the diary, if present.

        Args:
            appointment (str): The appointment to be removed.
        """
        if appointment in self.appointments:
            self.appointments.remove(appointment)

    def get_all_appointments(self):
        """Retrieves all appointments stored in the diary.

        Returns:
            list: A list containing all appointments.
        """
        return self.appointments
    
    def cancel_appointment(self, appointment_to_cancel):
        """Cancels a specific appointment from the diary, if present.

        Args:
            appointment_to_cancel (str): The appointment to be canceled.
        """
        if appointment_to_cancel in self.appointments:
            self.appointments.remove(appointment_to_cancel)
