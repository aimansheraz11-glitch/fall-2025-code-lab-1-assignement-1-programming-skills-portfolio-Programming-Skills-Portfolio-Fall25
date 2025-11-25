"""
## Exercise 5: Days of the Month - 30 Marks

Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.
"""
month_days = {
    1: 31,  # January
    2: 28,  # Default for February
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}
month_input = input("Enter the month number (1-12): ")
if month_input.isdigit():
    if 1 <= int(month_input) <= 12:
        month = int(month_input)
        if month == 2:
            leap_year = input("Is it a leap year? (yes/no): ").strip().lower()
            if leap_year == "yes":
                print("February has 29 days.")
            else:
                print("February has 28 days.")
        else:
            print(f"Month {month} has {month_days[month]} days.")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
else:
    print ("Invalid input. Please enter a numeric value for a month.")