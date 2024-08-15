import random

# Choices for the game
choices = ["rock", "paper", "scissors"]

# Game introduction
print("Welcome to Rock-Paper-Scissors!")

while True:
    # Get player's choice
    player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()

    if player_choice == 'quit':
        print("Thanks for playing!")
        break

    # Validate player's choice
    if player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Get computer's choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the result
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
    else:
        result = "You lose!"

    # Display the result
    print(result)
