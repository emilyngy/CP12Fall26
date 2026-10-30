import random


# ---------------------------------------------------------
# Function 1: Display the game instructions
# ---------------------------------------------------------
def show_instructions():
    print("Welcome to Bulls and Cows game")
    print("Try guess a secret number made of 4 different digits (0-9)")
    print("Bulls: digits that are correct and in the correct position")
    print("Cows: digits that are in the secret but in the wrong position")
    """
    Display a welcome message and explain the rules.

    TODO:
    - Welcome the player.
    - Explain that the secret contains 4 different digits.
    - Explain what Bulls and Cows mean.
    """


# ---------------------------------------------------------
# Function 2: Generate the secret number
# ---------------------------------------------------------
def generate_secret():
    number = [random.randint(0, 9) for _ in range(4)]
    while has_duplicates(number):
        number = [random.randint(0, 9) for _ in range(4)]
    return number


# ---------------------------------------------------------
# Function 3: Get the player's guess
# ---------------------------------------------------------
def get_guess():
    player_guess = []
    n = 4
    for i in range(n):
        guesses = int(input(f"Enter digit {i+1}: "))
        player_guess.append(guesses)
    return player_guess


# ---------------------------------------------------------
# Function 4: Check for duplicate numbers
# ---------------------------------------------------------
def has_duplicates(numbers):
    return len(numbers) != len(set(numbers))

# ---------------------------------------------------------
# Function 5: Check whether the guess is valid
# ---------------------------------------------------------
def is_valid_guess(guess):
    if len(guess) != 4:
        return False
    for number in guess:
        if number < 0 or number > 9:
            return False
    if has_duplicates(guess):
        return False
    return True



# ---------------------------------------------------------
# Function 6: Count Bulls
# ---------------------------------------------------------
def count_bulls(secret, guess):
    bulls = 0
    for i in range(4):
        if secret[i] == guess[i]:
            bulls += 1
    return bulls


# ---------------------------------------------------------
# Function 7: Count Cows
# ---------------------------------------------------------
def count_cows(secret, guess):
    cows = 0
    for i in range(4):
        if guess[i] in secret and guess[i] != secret[i]:
            cows += 1
    return cows


# ---------------------------------------------------------
# Function 8: Display the results
# ---------------------------------------------------------
def show_result(bulls, cows):
    print("Bulls:", bulls)
    print("Cows:", cows)
    """
    Print the number of Bulls and Cows.

    Example:
        show_result(2, 1)

    Output:
        Bulls: 2
        Cows: 1
    """


# ---------------------------------------------------------
# Function 9: Check whether the player won
# ---------------------------------------------------------
def has_won(bulls):
    return bulls == 4


# ---------------------------------------------------------
# Function 10: Display the final message
# ---------------------------------------------------------
def show_final_message(attempts):
    print()
    print("Congratulations!")
    print("You guessed the secret in", attempts, "attempts!")
    """
    Congratulate the player and display the total
    number of attempts.

    Example:
        Congratulations!
        You guessed the secret in 6 attempts!
    """


# =========================================================
# MAIN GAME
# =========================================================

def main():

    show_instructions()

    secret = generate_secret()

    attempts = 0
    won = False

    while not won:

        print()
        print("--------------------------")
        print("Attempt:", attempts + 1)

        guess = get_guess()

        # Keep asking until the player enters a valid guess.
        while not is_valid_guess(guess):
            print("Invalid guess! Please try again.")
            guess = get_guess()

        attempts += 1

        bulls = count_bulls(secret, guess)
        cows = count_cows(secret, guess)

        show_result(bulls, cows)

        won = has_won(bulls)

    show_final_message(attempts)


# Start the game
main()