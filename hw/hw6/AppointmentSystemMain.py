# AppointmentSystemMain.py
# Name: Xujia Qin
# Email: qin.xuj@northeastern.edu
# Date: Dec 8th, 2023

from datetime import *
from UserClass import *
from TimeClass import *
from DateClass import *
from AppointmentClass import *
from AppointmentDiaryClass import *

def add_user(users):
    """
    Add a new user to the system.

    Parameters:
    - users (dict): Dictionary containing user information.

    Returns:
    - users (dict): Updated dictionary after adding a new user or without any changes.
    """
    username = input("Enter username: ").strip().lower()  # Consider usernames as case insensitive

    # Check for valid characters in the username
    if not username.replace('.', '').replace('_', '').isalnum():
        print("Invalid characters in the username. Please use only alphabets, numbers, dots, and underscores.")
        return users

    # Check if the username already exists
    if username in users:
        print("Username already exists. Please choose another username.")
    else:
        # Add the new user to the UserClass
        new_user = User(username)  # Assuming User class exists
        users[username] = new_user  #assign the object 
        print(f"User {username} added successfully.")
    return users

def del_user(users):
    """
    Delete an existing user from the system.

    Parameters:
    - users (dict): Dictionary containing user information.

    Returns:
    - users (dict): Updated dictionary after deleting a user or without any changes.
    """
    username = input("Enter the username to delete: ").strip().lower()# Get the username to be deleted
    if username in users: # Check if the username exists in the dictionary
        del users[username] # Delete the user from the dictionary
        print(f"User {username} deleted successfully.")
    else:
        print("User not found.") # Return the updated dictionary after deletion or the unchanged dictionary

def list_user(users):
    """
    List all existing users in the system.

    Parameters:
    - users (dict): Dictionary containing user information.

    Returns:
    user_list if there are users
    """
    if users:  # Check if there are users in the dictionary
        user_list = sorted(users.keys())  # Get a sorted list of usernames
        print(user_list) # Print the list of usernames
    else:
        print("No users found.") # Print a message if there are no users in the dictionary
            
def check_username(users, username):
    """
    Check if the provided username exists in the user dictionary.

    Parameters:
    - users (dict): Dictionary containing user information.
    - username (str): Username to be checked.

    Returns:
    - bool: True if the username exists in the user dictionary, False otherwise.
    """
    if users and username in users: # Check if the username does not exist in the dictionary
        return True # Return True if the username exists in the dictionary
    else:
        print("Error: Invalid user.") # Print an error message for an invalid username
        return False


def check_date(date):
    """
    Check the validity of the date format (YYYY-MM-DD).

    Parameters:
    - date (str): Date string to be checked.

    Returns:
    - bool: True if the date is in the correct format, False otherwise.
    """
    try:
        year, month, day = map(int, date.split('-')) # Split the date string into year, month, and day
        datetime(year, month, day)  # Attempt to create a datetime object using the input date
    except ValueError: # Handle ValueError for invalid date format
        print("Error: Invalid date format.")# Print an error message for an invalid date
        return False
    return True  # Return True if the date format is valid

        
def schedule_appointment(users):
    """
    Schedule an appointment for a user.

    Parameters:
    - users (dict): Dictionary containing user information.

    Returns:
    String: the message that if the appointment is scheduled or not
    """
    username = input("Enter username: ").strip().lower()# Get the username to identify the user
    if not check_username(users, username):# Check if the username exists in the system
        return  # Exit if the username is invalid
    
    date = input("Enter date: ").strip()# Get the date for the appointment
    if not check_date(date):  # Validate the date format
        return
    
    start_time = parse_time(input("Enter start time: ").strip())# Get the start time for the appointment
    if start_time is None:
        print("Error: Invalid start time format.")
        return
    
    user = users[username]  # Retrieve the user object
    appointments = user.get_appointment_diary().get_all_appointments()# Get all appointments for the user
    # Check for appointment conflict for start_time 
    for appointment in appointments:
        if appointment.date == date and appointment.start_time <= start_time < appointment.end_time:
            print("Error: Appointment time conflicts with an existing appointment.")
            return

    end_time = parse_time(input("Enter end time: ").strip()) # Get the end time for the appointment

    if end_time is None:
        print("Error: Invalid end time format.")
        return
    if end_time <= start_time: # Check if the end time is before or equal to the start time
        print("Error: End time should be later than the start time.") 
        return

    # Check for appointment conflict
    for appointment in appointments:
        if appointment.date == date and (appointment.start_time < end_time <= appointment.end_time or is_time_windonw_within_range(start_time, end_time, appointment.start_time, appointment.end_time)):
            print("Error: Appointment time conflicts with an existing appointment.")
            return
        
    purpose = input("Enter purpose: ").strip()# Get the purpose of the appointment

    # Create a new appointment object
    new_appointment = Appointment(date, start_time, end_time, purpose)
    users[username].get_appointment_diary().add_appointment(new_appointment)
    print("Appointment added successfully.")# Confirm that the appointment has been scheduled
    
def cancel_appointment(users):
    """
    Cancel an existing appointment for a user.

    Parameters:
    - users (dict): Dictionary containing user information.

    Returns:
    String: the message that if the appointment is canceld or not
    """
    username = input("Enter username: ").strip().lower()
    if not check_username(users, username):
        return
    # User prompt the date of the appointment to cancel
    date = input("Enter date: ").strip()
    # Check for valid date format (YYYY-MM-DD)
    if not check_date(date):
        return
    
    start_time = parse_time(input("Enter start time: ").strip())
    if start_time is None:
        print("Error: Invalid start time format.")
        return
    end_time = parse_time(input("Enter end time: ").strip())
    if end_time is None:
        print("Error: Invalid end time format.")
        return

    if end_time <= start_time: # Ensure that the end time is after the start time
        print("Error: End time should be later than the start time.") 
        return
    
    
    user = users[username]
    appointments = user.get_appointment_diary().get_all_appointments()
    
    appointment_to_cancel = None
    for appointment in appointments:
         # Check for an appointment matching the provided date, start time, and end time
        if appointment.date == date and appointment.start_time == start_time and appointment.end_time == end_time:
            appointment_to_cancel = appointment
            break

    if appointment_to_cancel:# If a matching appointment is found
        # Cancel the appointment if found
        user.get_appointment_diary().cancel_appointment(appointment_to_cancel)
        print("Appointment canceled successfully.")
    else: # If no matching appointment is found
        print("Error: No matching appointment found.")
    
def check_appointment(users):
    """
    Check for an appointment for a user on a specific date and time.

    Parameters:
    - users (dict): Dictionary containing user information.

    Returns:
    String: appoints found on certain date between certain start and end time
    """
    username = input("Enter username: ").strip().lower()
    if not check_username(users,username):
        return
    
    date = input("Enter date: ").strip()
    # Check for valid date format (YYYY-MM-DD)
    if not check_date(date):
        return
    
    start_time = parse_time(input("Enter start time: ").strip())

    if start_time is None:
        print("Error: Invalid start time format.")
        return
  
    
    appointments = users[username].get_appointment_diary().get_all_appointments()# Get all appointments for the user
    appointment_found = False # Initialize a variable to track if an appointment is found

    for appointment in appointments:
        # Check for an appointment matching the provided date and start time
        if appointment.date == date and appointment.start_time == start_time:
            # Print the details of the found appointment
            print(f"Appointment found on {date} between {appointment.start_time} to {appointment.end_time}.")
            appointment_found = True # Set the flag to True as appointment is found
            break

    if not appointment_found:
        print("No appointment found.")
    
def retrieve_purpose(users):
    """
    Retrieve the purpose of an appointment for a user at a specific date and time.

    Parameters:
    - users (dict): Dictionary containing user information.

    Returns:
    String: purpose
    """
    username = input("Enter username: ").strip().lower()
    if not check_username(users,username):
        return
    
    date = input("Enter date: ").strip()
    # Check for valid date format (YYYY-MM-DD)
    if not check_date(date):
        return
    start_time = parse_time(input("Enter start time: ").strip())

    if start_time is None:
        print("Error: Invalid start time format.")
        return
    
    end_time = parse_time(input("Enter end time: ").strip())
    if end_time is None:
        print("Error: Invalid end time format.")
        return
    if end_time <= start_time:
        print("Error: End time should be later than the start time.") 
        return
    
    appointments = users[username].get_appointment_diary().get_all_appointments() # Get all appointments for the user
    
    # Check if any appointments exist on the specified date
    found_appointment = False
    for appointment in appointments:
        # Check for an appointment matching the provided date, start time, and end time
        if appointment.date == date and appointment.start_time == start_time and appointment.end_time == end_time:
            found_appointment = True
            print("The purpose of the appointment is: " + appointment.purpose)  
            return     
    if not found_appointment:
        print("No appointment found on " + str(date) + " start on " + str(start_time))
        return
    
    
def reschedule_appointment(users):
    """
    Reschedule an existing appointment for a user.

    Parameters:
    - users (dict): Dictionary containing user information.

    Returns:
    String: the message that if the appoint is scheduled or not
    """
    # Prompt user for the username
    username = input("Enter username: ").strip().lower()
    if not check_username(users,username):
        return
    # Prompt user for the date
    date = input("Enter date: ").strip()
    # Check for valid date format (YYYY-MM-DD)
    if not check_date(date):
        return
    # Retrieve appointments for the specified user
    appointments = users[username].get_appointment_diary().get_all_appointments()
    
    # Check if any appointments exist on the specified date
    found_appointment = False
    for appointment in appointments:
        if appointment.date == date:
            found_appointment = True
            # You may perform other actions if an appointment is found on the given date

    if not found_appointment:
        print("No appointment found on " + str(date))
        return
    # Prompt user for the start time
    start_time = parse_time(input("Enter start time: ").strip())
    if start_time is None:
        print("Error: Invalid start time format.")
        return
    
    # Check if an appointment exists at the specified start time
    found_appointment = False
    for appointment in appointments:
        if appointment.start_time == start_time:
            found_appointment = True
            # You may perform other actions if an appointment is found on the given date

    if not found_appointment:
        print("No appointment found on " + str(start_time))
        return
    
     # Prompt user for the end time
    end_time = parse_time(input("Enter end time: ").strip())
    if end_time is None:
        print("Error: Invalid end time format.")
        return
    
    # Check if the end time is before or equal to the start time
    if end_time <= start_time:
        print("Error: End time should be later than the start time.") 
        return
    # Check if any appointment exists at the specified end time
    found_appointment = False
    for appointment in appointments:
        if appointment.end_time == end_time:
            found_appointment = True
    if not found_appointment:
        print("no appointment found")
        return
    else:
        # Prompt user for the new date
        new_date = input("Enter the new date: ").strip()
        # Check for valid date format (YYYY-MM-DD)
        if not check_date(new_date):
            return
        # Check for conflicts with the new appointment timings
        new_starttime = parse_time(input("Enter start time: ").strip())
        if new_starttime is None:
            print("Error: Invalid new start time format.")
            return
        # Check for conflicts with the new appointment timings
        if appointment.date == new_date and appointment.start_time <= new_starttime < appointment.end_time:
            print("Error: Appointment time conflicts with an existing appointment.")
            return
        new_endtime = parse_time(input("Enter end time: ").strip())
        if new_endtime is None:
            print("Error: Invalid new end time format.")
            return
        # Check if the new end time is before or equal to the new start time
        if new_endtime <= new_starttime:
            print("Error: End time should be later than the start time.") 
            return
        # Check for conflicts with the new appointment timings
        if appointment.date == new_date and (appointment.start_time < new_endtime <= appointment.end_time or is_time_windonw_within_range(new_starttime, new_endtime, appointment.start_time, appointment.end_time)):
            print("Error: Appointment time conflicts with an existing appointment.")
            return
        # Find the appointment to reschedule
        appointment_to_reschedule = None
        for appointment in appointments:
            if appointment.date == date and appointment.start_time == start_time and appointment.end_time == end_time:
                appointment_to_reschedule = appointment
                break
        if appointment_to_reschedule:

        # Reschedule the appointment to the new date and time
            appointment_to_reschedule.date = new_date
            appointment_to_reschedule.start_time = new_starttime
            appointment_to_reschedule.end_time = new_endtime
            
            print("Appointment rescheduled successfully.")
        else:
            print("Error: No matching appointment found for rescheduling.")
    
def is_time_windonw_within_range(check_start_time, check_end_time, start_time, end_time): # check_start_time > end_time or check_end_time < start_time
    """
    Check if a specific time window is within the range of start_time and end_time.

    Parameters:
    - check_start_time (Time): Start time of the window to be checked.
    - check_end_time (Time): End time of the window to be checked.
    - start_time (Time): Start time of the range.
    - end_time (Time): End time of the range.

    Returns:
    - bool: True if the time window is within the range, False otherwise.
    """
    return (check_start_time < end_time) and (check_end_time > start_time)


def parse_time(time_str):
    """
    Parse a string into a Time object representing a specific time.

    Parameters:
    - time_str (str): Time string to be parsed.

    Returns:
    - Time or None: Time object if the parsing is successful, None otherwise.
    """
    # Split the time string by whitespace
    time_split = time_str.split()
    
    # Check if the time format is 9 am/9 AM/9 pm/9 PM
    if len(time_split) == 2 and time_split[0].isdigit() and time_split[1].upper() in ['AM', 'PM']:
        try:
            # Extract hours and validate
            hours = int(time_split[0])
            if 1 <= hours <= 12:
                period = time_split[1].upper()
                # Return Time object with minutes set to 0 for formats like '9 am'
                return Time(hours, 0, period)  # Set minutes to 0 for formats like '9 am'
        except ValueError:
            pass
    
    # Check if the time format is 11:00 AM/am/PM/pm
    if len(time_split) == 2:
        # Split hours and minutes
        hours_minutes = time_split[0].split(':')
        if len(hours_minutes) == 2:
            try:
                # Extract hours and minutes, and validate
                hours = int(hours_minutes[0])
                minutes = int(hours_minutes[1])
                
                if 1 <= hours <= 12 and 0 <= minutes <= 59:
                    period = time_split[1].upper()
                    if period in ['AM', 'PM']:
                         # Return Time object if all conditions are met
                        return Time(hours, minutes, period)
            except ValueError:
                pass
    return None # Return None if time string parsing is unsuccessful

    

def start():
    """
    Start the Appointment Management System
    """
    users = {}  # Initialize an empty dictionary to store users

    print("Welcome to Appointment Management System! What would you like to do?")
    while True:
        print("- [a] Add new user")
        print("- [d] Delete an existing user")
        print("- [l] List existing users")
        print("- [s] Schedule an appointment")
        print("- [c] Cancel an appointment")
        print("- [f] Check for appointment on certain date and time")
        print("- [p] Retrieve purpose of an appointment")
        print("- [r] Reschedule an existing appointment")
        print("- [x] Exit the system")

        # Get user input for the desired option
        choice = input("Enter the character in square brackets for the desired option: ").strip().lower()

        # Perform actions based on user's choice
        if choice == 'a':
            users = add_user(users)
        elif choice == 'd':
            users = del_user(users)
        elif choice == 'l':
            list_user(users)
        elif choice == 's':
            schedule_appointment(users)
        elif choice == 'c':
            cancel_appointment(users)
        elif choice == 'f':
            check_appointment(users)
        elif choice == 'p':
            retrieve_purpose(users)
        elif choice == 'r':
            reschedule_appointment(users)
        elif choice == 'x':
            print("Exiting the system. Goodbye!")
            break  # Exit the system if the user chooses to do so
        else:
            print("Invalid Option")  # Display message for an invalid option

if __name__ == "__main__":
    start()  # Start the appointment management system
       



            
        
        