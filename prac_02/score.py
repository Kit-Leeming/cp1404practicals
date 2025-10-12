"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

def main():
    score = float(input("Enter score: "))
    result = calculate_result(score)
    print(result)
    random_score = generate_random_score()
    random_result = calculate_result(random_score)
    print(f"Random results: {random_result}")


def calculate_result(score: float) -> str:
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


def generate_random_score():
    score = random.randint(0,100)
    return score


main()
