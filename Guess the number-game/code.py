import random

def number_guessing_game():
    print(" Welcome to the Number Guessing Game!")
    
    # Get difficulty level before the game starts
    level = input("Choose difficulty (easy/hard): ").lower()
    if level == "easy":
        max_range = 100
        max_attempts = 10
    else:
        max_range = 500
        max_attempts = 7

    # Generate a random number
    secret_number = random.randint(1, max_range)
    print(f"I'm thinking of a number between 1 and {max_range}. You have {max_attempts} attempts.")

    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f" Correct! The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

    else:
        print(f"You're out of guesses. The number was {secret_number}. Better luck next time!")

# Running the game
if __name__ == "__main__":
    number_guessing_game()
