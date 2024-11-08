import random
import time
import Questions as qu

# Global variable to store the user's name
user_name = None

def start_new_game():
    """Function to start a new game and ask two riddles."""
    global user_name
    score = 0

    # Welcome the user and start the game
    if user_name:
        print(f"\nWelcome back, {user_name}! Let's start the game...")
    else:
        print("\nStarting a new game...")

    # Select two random riddles to ask
    # print(riddle["question"])

    for i in range(2):
        riddle_key = random.choice(list(qu.riddles.keys()))
        riddle = qu.riddles[riddle_key]
        print(f"\nRiddle {i}: {riddle['question']}")
        user_answer = input("Your answer: ").strip().lower()

        # Check if the answer is correct
        if user_answer == riddle['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was '{riddle['answer']}'.")
            # Offer a clue if the answer was wrong
            print("Clue:", riddle["clue"])
            user_answer = input("Try again: ").strip().lower()
            if user_answer == riddle["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect again. The answer was '{riddle['answer']}'.")

    # Display the final score after two riddles
    print(f"\nGame Over! Your score: {score}/2")
    time.sleep(1)  # Small pause before returning to menu

def add_user_name():
    """Function to add or update the user's name."""
    global user_name
    user_name = input("Please enter your name: ").strip()
    print(f"Name set to: {user_name}")

def exit_game():
    """Function to exit the game."""
    print("Exiting the game. Goodbye!")
    exit(0)

def display_menu():
    """Function to display the main menu."""
    print("\nMain Menu:")
    print("1. Start New Game")
    print("2. Add User’s Name")
    print("3. Exit Game")

def main():
    while True:
        display_menu()
        choice = input("Please select an option (1-3): ").strip()

        if choice == "1":
            start_new_game()
        elif choice == "2":
            add_user_name()
        elif choice == "3":
            exit_game()
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
