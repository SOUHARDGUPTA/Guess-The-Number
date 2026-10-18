
import random

# Choose a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

print("================================")
print("     NUMBER GUESSING GAME")
print("================================")
print("I have selected a number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid whole number!")
        continue

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! Try a higher number.")
    elif guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        print(f"Congratulations! You guessed it: {secret_number}")
        print(f"Total attempts: {attempts}")
        break

print("Thanks for playing!")
