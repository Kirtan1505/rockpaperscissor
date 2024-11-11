import random

def main():
    print("Welcome to Rock Paper Scissors!")
    print("Here are the rules:")
    print("1. Rock beats Scissors")
    print("2. Scissors beats Paper")
    print("3. Paper beats Rock")
    print("4. If both players select the same option, it's a tie.")

    # Continue playing until there's no tie
    while True:
        # Get user choice
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        
        # Randomly select the computer's choice
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)

        # Print both choices
        print(f"You chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie! Let's rematch...\n")
            continue  # Restart the loop if it's a tie
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            break  # End the game when the user wins
        else:
            print("You lose!")
            break  # End the game when the user loses

if __name__ == "__main__":
    main()
