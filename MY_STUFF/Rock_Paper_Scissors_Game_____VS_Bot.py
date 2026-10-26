import random

Score = 0

while True:
    user_action = input("\nEnter a choice Rock, Paper or Scissors: ").lower()
    if user_action != "rock" or "paper" or "scissors":
        possible_action = ["Rock", "Paper", "Scissors"]
        computer_action = random.choice(possible_action).lower()
        print(f"\nYou chose {user_action} and computer chose {computer_action}")

        if user_action == computer_action:
            print(f"Both players chose {user_action}. It is a tie.")
            print(f"Score: {Score}")
        elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock vs Scissors You Win")
                Score += 1
                print(f"Your score is {Score}")
            else:
                print("Rock vs Paper You Lose")
                print("End of game")
                print(f"Your score was {Score}")
                play_again = input("\nPlay Again? Y/n: ").lower()
                Score = 0
                if play_again != "y":
                    break
        elif user_action == "scissors":
            if computer_action == "paper":
                print("Scissors vs Paper You Win")
                Score += 1
                print(f"Your score is {Score}")
            else:
                print("Scissors vs Rock You Lose")
                print("End of game")
                print(f"Your score was {Score}")
                play_again = input("\nPlay Again? Y/n: ").lower()
                Score = 0
                if play_again != "y":
                    break
        elif user_action == "paper":
            if computer_action == "rock":
                print("Paper vs Rock You Win")
                Score += 1
                print(f"Your score is {Score}")
            else:
                print("Paper vs Scissors You Lose")
                print("End of game")
                print(f"Your score was {Score}")
                play_again = input("\nPlay Again? Y/n: ").lower()
                Score = 0
                if play_again != "y":
                    break
    else:
        print("Enter Rock, Paper or Scissors")