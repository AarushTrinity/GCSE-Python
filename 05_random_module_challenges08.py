import random  # We need this to generate random numbers

# Step 1: Initialize the score
score = 0

# Step 2: Start the loop for 5 questions
for i in range(5):  # Loop 5 times (0, 1, 2, 3, 4)
    
    # Step 3: Generate two random numbers
    num1 = random.randint(1, 20)  # Random number between 1 and 20
    num2 = random.randint(1, 20)  # Another random number between 1 and 20
    
    # Step 4: Ask the question
    print(f"Question {i + 1}: What is {num1} + {num2}?")  # i + 1 to start question numbers at 1
    
    # Step 5: Get the user's answer
    answer = int(input("Your answer: "))
    
    # Step 6: Check if the answer is correct
    if answer == num1 + num2:
        print("Correct!")
        score += 1  # Add 1 to the score
    else:
        print(f"Wrong! The answer was {num1 + num2}")

# Step 7: Tell the player their score
print(f"You got {score} out of 5 questions correct.")
