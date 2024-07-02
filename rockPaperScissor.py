import random

def get_user_choice():
    """
    Prompt the user to choose rock, paper, or scissors.
    """
    while True:
        user_choice = input("Choose rock (r), paper (p), or scissors (s): ").lower()
        if user_choice in ['r', 'p', 's']:
            return user_choice
        else:
            print("Invalid input. Please enter r, p, or s.")

def get_computer_choice():
    """
    Generate a random choice (rock, paper, or scissors) for the computer.
    """
    choices = ['r', 'p', 's']
    computer_choice = random.choice(choices)
    return computer_choice
