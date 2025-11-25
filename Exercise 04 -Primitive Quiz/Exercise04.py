"""
## Exercise 4: Primitive Quiz - 30 Marks

In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
1. Write a program that asks the user "What is the capital of France?" and waits for their response.
2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the answer is wrong.

### Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.
"""
question = "What is the capital of France? "
answer = input(question)
if answer.strip().lower() == "paris":
    print("Correct!")
else:
    print("Wrong answer.")
    quiz = {
        "What is the capital of Germany? ": "berlin",
        "What is the capital of Italy? ": "rome",
        "What is the capital of Spain? ": "madrid",
        "What is the capital of Portugal? ": "lisbon",
        "What is the capital of Netherlands? ": "amsterdam",
        "What is the capital of Belgium? ": "brussels",
        "What is the capital of Austria? ": "vienna",
        "What is the capital of Switzerland? ": "bern",
        "What is the capital of Sweden? ": "stockholm"
    }
    score = 0
    for country, capital in quiz.items():
        user_answer = input(country)
        if user_answer.strip().lower() == capital:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {capital.capitalize()}.")