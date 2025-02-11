#Create a variable called "compnum"and set it to 50
compnum = 50
#Ask the user to make a guess
guess = int( input("Please guess the number I am thinking "))
#Create a variable called count and set it to 1
count = 1



#While their guess is not the same as the compnum value, tell them that if their guess is too low or too high
while guess != compnum:
    if guess > compnum:
        print("Too high")
    elif guess < compnum:
        print("Too low")
    
#Ask the user to make another guess
    guess = int(input("Guess again: "))
#Count must increment by 1 every time the user has a guess
    count += 1
#Ask them if they want another guess
    guess = input("Would you like another guess? (y/n)")
    
    if guess == "y":
        guess = int(input("Guess again: "))
        count += 1
    elif guess == "n":
        ##If they enter the same value as compnum, display the message "well done, you took {count} attempts"

        print("Well done, you took", count, "attempts.")
        
        #end loop
        break

#If they enter the same value as compnum, display the message "well done, you took {count} attempts"
print("Well done, you took", count, "attempts.")
        


    
