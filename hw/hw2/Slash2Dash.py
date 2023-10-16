# Slash2Dash.py
# Name: Xujia Qin
# Email: qin.xuj@northeastern.edu
# Date: Oct 13th, 2023
"""This program is to solicit a date string in slash format and then displays the equivalent date in dash format"""
"""The input will be the a date string in slash format, and we will return the date string in the dash format as our output"""

"""The initial step should use input() to store the incoming slash-date string in a
variable (say s) and then compute the location of the two slashes. """

# Input slash-formatted date
# Remove leading and trailing single quotes and double quotes if present
slash_date = input("Enter a slash-formatted date (MM/DD/YYYY): ").strip('\'"')


# Initialize variables to store the two slash indices as flags
first_slash_index = -1
second_slash_index = -1

# Find the indices of the slashes
for i in range(len(slash_date)):
    if slash_date[i] == "/":
        if first_slash_index == -1:
            first_slash_index = i #flip the flag sign if we find the first index then, after this, only the second index's flag is -1
        else:
            second_slash_index = i #flip the flag sign #if we find the second index

try:
    # Check if both slashes were found
    if first_slash_index == -1 or second_slash_index == -1:
        raise ValueError("Invalid input: Please enter a valid slash-formatted date.") #if the input has no "/", then there will be an error message presented

    else:
        month_slice = slash_date[:first_slash_index] #the index from 0 to first_slash_index excluded belongs to month slice
        day_slice = slash_date[first_slash_index + 1 : second_slash_index]#the index from first_slash_index + 1 to second_slash_index excluded belongs to month slice
        year_slice = slash_date[second_slash_index + 1:] #the index from second_slash_index + 1 to the last index excluded belongs to month slice

    # Check if month, day, and year slices contain only digits
    if not(month_slice.isdigit() and day_slice.isdigit() and year_slice.isdigit()) :
        raise ValueError("Invalid input: Date components must contain only digits.")
    # Check if month, day, and year slices's length are reasonable
    elif not (0 < len(month_slice)<=2 and 0 < len(day_slice)<= 2):
        raise ValueError("Invalid input: the length of day, month must be <= 2 and > 0.")
    elif not(len(year_slice)== 4 or len(year_slice)== 2):
        raise ValueError("Invalid input: the length of year must be 2 or 4.")
        

    else:
        # Convert month and day slices if needed
        if len(month_slice) == 1:
            month_slice = '0' + month_slice #concatenate "0" in the beginning
        if len(day_slice) == 1:
            day_slice = '0' + day_slice #concatenate "0" in the beginning

        # Convert the year slice based on the rules
        if len(year_slice) == 2:
            if int(year_slice) <= 23:
                year_slice = '20' + year_slice
            else:
                year_slice = '19' + year_slice

        # Concatenate and create the dash-formatted date
        dash_date = month_slice + '-' + day_slice + '-' + year_slice

        # Display the result
        print("Enter a valid slash-date:", slash_date,"  ", dash_date)
except ValueError as e: # print the error message
    print(e)
