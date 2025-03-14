import random

# 1. Generate a random number
num = random.randint(1, 5)  

# 2. Ask the user for their first guess
guess1 = int(input("Guess a number between 1 and 5: ")) 

# 3. Check the first guess
if guess1 == num:
    print("Well done!")
else:
    # 4. Give a hint
    if guess1 < num:
        print("Too low!")
    else:
        print("Too high!")

    # 5. Ask for the second guess
    guess2 = int(input("Try again: "))

    # 6. Check the second guess
    if guess2 == num:
        print("Correct!")
    else:
        print("You lose!")
