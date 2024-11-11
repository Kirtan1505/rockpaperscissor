import random

def main():
    print("Welcome to Rock Paper Scissors!")
    print("Here are the rules:")
    print("1. Rock beats Scissors")
    print("2. Scissors beats Paper")
    print("3. Paper beats Rock")
    print("4. If both players select the same option, it's a tie.")
    
    # Get user choice
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    # Randomly select the computer's choice
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    # Print both choices
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")

if __name__ == "__main__":
    main()
