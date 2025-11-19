import random

# Generate random number between 1 and 20
secret_number = random.randint(1, 20)

print("I'm thinking of a number between 1 and 20...")

while True:
    # Ask for guess
    guess = input("Take a guess: ")

    # Convert guess to int
    guess = int(guess)

    # Compare guess to secret number
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("You got it! Great job.")
        break # Exit loop