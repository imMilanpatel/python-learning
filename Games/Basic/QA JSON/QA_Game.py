# This python file will read the Questions from JSON file and compare it with JSON value and print the result.
import json
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'QA.json')

# Open the JSON file in the same directory as the script
with open(json_path, 'r', encoding='utf-8') as file:
    # Load the JSON content
    data = json.load(file)

# Access the questions
questions = data["questions"]

# Game loop
while True:
    total = 0
    for qna in questions:
        print("Question:", qna["question"])
        answer = input("Your answer: ")
        if answer.strip().lower() == qna["answer"].strip().lower():
            print("That's correct!")
            total += 1
            print(f"Your Current Score is: {total}")
        else:
            print("INCORRECT :(")

    print(f"Final Score: {total}")
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.strip().lower() != 'y':
        break