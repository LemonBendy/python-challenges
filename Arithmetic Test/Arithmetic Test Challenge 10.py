import secrets
import json
from random import randint


def load_file() -> object:
    with open("scores.json", "r") as f:
        results_arr = json.load(f)
    return results_arr


def write_file(data) -> None:
    with open("scores.json", "w") as f:
        json.dump(results_arr, f, indent=2)

        
def print_leaderboard():
    data = load_file()
    accuracies = {key: value["correct"] / (value["incorrect"] + value["correct"]) for key, value in data.items()}
    accuracy_tuples = [(k, v) for k, v in accuracies.items()]
    sorted_names = [n[0] for n in list(reversed(sorted(accuracy_tuples, key=lambda i: i[1])))]
 
    for name in sorted_names:
        print(f"\033[32m{name}\033[0m\n-> Correct: {data[name]['correct']}\n-> Incorrect: {data[name]['incorrect']}")
        print(f"-> Accuracy: {round(accuracies[name] * 100, 2)}%\n")


def random_int(x):
    n1 = randint(0, x)
    n2 = randint(0, x)
    return n1, n2


def multiple(question_number):
    n1, n2 = random_int(12)
    question = int(input(str(question_number) + ". What is " + str(n1) + " x " + str(n2) + ": "))
    correct = n1*n2
    return question == correct


def addition(question_number):
    n1, n2 = random_int(99)
    question = int(input(str(question_number) + ". What is " + str(n1) + " + " + str(n2) + ": "))
    correct = n1+n2
    return question == correct


def subtraction(question_number):
    n1, n2 = random_int(99)
    question = int(input(str(question_number) + ". What is " + str(n1) + " - " + str(n2) + ": "))
    correct = n1-n2
    return question == correct


def division(question_number):
    n1 = randint(0, 99)
    nums = (1, 2, 4, 5, 8, 10)
    n2: int = secrets.choice(nums)
    question = float(input(str(question_number) + ". What is " + str(n1) + " ÷ " + str(n2) + ": "))
    correct = n1/n2
    return question == correct


def select(num, question):
    return [addition, multiple, division, subtraction][num](question)


name = input("Name: ")

correct = 0
questions = 3

for x in range(questions):
    rand = randint(0, 3)
    if select(rand, x + 1):
        correct += 1
        print("\033[32mCorrect!\033[0m\n")
    else:
        print("\033[31mIncorrect :(\033[0m\n")

print(f"You got {correct} correct and {questions - correct} incorrect")

results_arr = load_file()
if name in results_arr:
    results_arr[name]["correct"] += correct
    results_arr[name]["incorrect"] += questions - correct
else:
    results_arr[name] = {
        "correct": correct,
        "incorrect": questions - correct
    }

write_file(results_arr)
print_leaderboard()

# Worked on by Ryan and Ben in personal tasks 18/10/22
