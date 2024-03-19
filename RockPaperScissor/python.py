import random

def get_user_choice():
    """Prompt the user to choose rock, paper, or scissors."""
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    """Generate a random choice (rock, paper, or scissors) for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's choice and the computer's choice."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    """Main function to run the Rock-Paper-Scissors game."""
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nRock-Paper-Scissors Game")
        print("Enter 'quit' to end the game.")
        
        user_choice = get_user_choice()
        if user_choice == 'quit':
            break
        
        computer_choice = get_computer_choice()
        
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        print(f"\nScore: You - {user_score}, Computer - {computer_score}")
        
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
