# set the variable bottles to the value of 10
bottles = 10

#Using the song "10 green bottles", display the lines
#"There are {number} green bottles hanging on the wall, {number} green bottles hanging on the wall, and if one green bottle should accidentally fall"
while bottles > 0:
    print("There are", bottles, "green bottles hanging on the wall,")
    print(bottles, "green bottles hanging on the wall,")
    print("And if one green bottle should accidentally fall,")

    while True:
        try:
            #Then ask the user "How many green bottles will be hanging on the wall? "
            answer = int(input("How many green bottles will be hanging on the wall? "))
            
            #If they answer correctly, display the message "No, try again" until they get it right.
            if answer == bottles - 1:
                bottles -= 1
                print("There'll be", bottles, "green bottles hanging on the wall.")
                break
            else:
                print("No, try again.")
        except ValueError:
            print("That's not a number. Try again.")

#When the number of green bottles gets down to 0, display the message "There'll be no green bottles hanging on the wall"
if bottles == 0:
    print("There'll be no green bottles hanging on the wall.")
