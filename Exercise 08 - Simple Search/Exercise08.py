"""
## Exercise 8: Simple Search - 30 Marks

Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

### Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.
"""
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search_name = "Sam"
if search_name in names:
    print(f"{search_name} found in the list!")
else:
    print(f"{search_name} not been found in the list.")
# Optional Requirement
user_input = input("Enter the name to search for: ")
if user_input in names:
    print(f"{user_input} found in the list!")
else:
    print(f"{user_input} not been found in the list.")
