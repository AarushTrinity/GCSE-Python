import random  # Step 1: Import the random module

# Step 2: Generate a random number
num = random.randint(1, 10)  

# Step 3: Set 'correct' to False 
correct = False

# Step 4: Start the guessing loop
while not correct:  # Keep looping as long as 'correct' is False
    guess = int(input("Guess the number (between 1 and 10): "))  # Get the user's guess

    # Step 5: Check if the guess is correct
    if guess == num:
        correct = True  # Set 'correct' to True to end the loop
        print("Congratulations! You guessed the number!")
    # Step 6: Check if the guess is too high
    elif guess > num:
        print("Too high!")
    # Step 7: Otherwise, the guess must be too low
    else:
        print("Too low!")
