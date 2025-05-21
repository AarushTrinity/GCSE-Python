import random

random_num = random.randint(1,10)
correct = False

while correct == False:
    guess = int(input("Guess the number"))
    if guess == random_num:
        correct = True
