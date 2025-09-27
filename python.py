import random

print("🎮 Welcome to the Number Guessing Game 🎮")
print("I have chosen a number between 1 and 10. Can you guess it?")

# Step 1: Generate a random number
secret_number = random.randint(1, 10)

# Step 2: Take user input
guess = int(input("Enter your guess (1-10): "))

# Step 3: Game logic using conditionals
if guess == secret_number:
    print("🎉 Congratulations! You guessed it right!")
elif guess > secret_number:
    print("Too high! Try a smaller number.")
else:
    print("Too low! Try a bigger number.")

print(f"(The secret number was: {secret_number})")
