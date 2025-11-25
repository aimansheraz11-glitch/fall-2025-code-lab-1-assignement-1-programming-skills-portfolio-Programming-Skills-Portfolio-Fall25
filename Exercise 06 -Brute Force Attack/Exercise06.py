"""
## Exercise 6: Brute Force Attack - 30 Marks

Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.

### Optional Requirements:

Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.
"""
correct_password = "12345"
password=input("Enter the password: ")
while password  != correct_password :
    print("Incorrect password. Try again please.")
    password=input("Enter the password: ")
print("Access granted!")
# Optional Requirement
attempts_remaining = 5
while attempts_remaining > 0:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        attempts_remaining -= 1
        if attempts_remaining > 0:
            print(f"Incorrect password. You have {attempts_remaining} attempts remaining.")
        else:
            print("Maximum attempts reached!  Authorities are now alerted.")
