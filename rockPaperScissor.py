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

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner based on the user's choice and the computer's choice.
    """
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    """
    Display the user's choice, the computer's choice, and the result.
    """
    print(f"User chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if winner == "user":
        print("User wins!")
    elif winner == "computer":
        print("Computer wins!")
    else:
        print("It's a tie!")

