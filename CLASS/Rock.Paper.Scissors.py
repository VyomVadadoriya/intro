import random

while True:
    user_action = input("\nEnter a choice Rock, Paper or Scissors: ").lower()
    possible_action = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_action).lower()
    print(f"\nYou chose {user_action} and computer chose {computer_action}")

    if user_action == computer_action:
        print(f"Both players chose {user_action}. It is a tie.")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock vs Scissors You Win")
        else:
            print("Rock vs Paper You Lose")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors vs Paper You Win")
        else:
            print("Scissors vs Rock You Lose")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock vs Scissors You Win")
        else:
            print("Rock vs Paper You Lose")

    play_again = input("\nPlay Again? Y/n: ").lower()
    if play_again != "y":
        break