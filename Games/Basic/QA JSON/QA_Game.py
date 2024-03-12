# This python file will read the Questions from JSON file and compare it with JSON value and print the result.
import json

# Open the JSON file
with open('python-learning\Games\Basic\QA JSON\QA.json', 'r') as file:
    # Load the JSON content
    data = json.load(file)

# Access the questions
questions = data["questions"]

# Game
game_status = True
while game_status:
    total = 0
    for qna in questions:
        print("Question", qna["question"])
        answer = input("Your answer: ")
        if answer == qna["answer"]:
            print("That's correct !")
            total += 1
            print(f"Your Current Score is: {total}")
        else:
            print("INCORRECT :(")

    print(f"Final Score: {total}")
    game_status = False