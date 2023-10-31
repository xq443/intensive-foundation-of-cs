# money_dispenser.py
# Name: Xujia Qin
# Email: qin.xuj@northeastern.edu
# Date: Oct 28th, 2023
""" This program is to uses the fewest number of bills and coins to dispense the specified amount of money. 
Only twenties ($20), tens ($10), fives ($5), ones ($1), quarters (25 cents), dimes (10 cents),
nickels (5 cents), and pennies (1 cents) will be used """
from decimal import Decimal
# Take user input for the amount of money
amount = Decimal(input("Enter amount: ")) #use decmial, because float numbers are stored as binary approximations of real numbers, which can lead to rounding errors.

# Convert to cents
amount_cents = int(amount * 100)

# Define denominations
denominations = [2000, 1000, 500, 100, 25, 10, 5, 1]
names = ["twenties", "tens", "fives", "ones", "quarters", "dimes", "nickels", "pennies"]

# New empty list to store the final result
results = []

# Calculate the number of each denomination
for i in range(len(denominations)):
    name = names[i]
    count = amount_cents // denominations[i]
    amount_cents %= denominations[i]

    # Singularize names if count is 1
    if count == 1:
        if name == "pennies":
            name = "penny"
        elif name == "twenties":
            name = "twenty"
        else:
            name = names[i][:-1]  # Remove the last character 's'

    if count > 0:
        results.append(str(count) + " " + name) #append every denomination and its count 

# Display the results in the sample output format
for result in results:
    print(result)

