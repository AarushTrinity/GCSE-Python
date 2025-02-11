#Ask which direction the user wants to count (up or down) i.e. "u" or "d"
direction = input("Do you want to count up or down? (u/d): ")

#If they select up, then ask them fo the top number and then count from 1 to that number
if direction == "u":
    top_number = int(input("Enter the number to count up to: "))
    for i in range(1, top_number + 1):
        print(i)
#If they select down, ask them to enter a number below 20 and then count down from 20 to that number
elif direction == "d":
    bottom_number = int(input("Enter a number below 20 to count down to: "))
    if bottom_number >= 20:
        print("Invalid input. Please enter a number below 20.")
    else:
        for i in range(20, bottom_number - 1, -1):
            print(i)
#If they entered something other than up or down, display the message "i don't understand"
else:
    print("I don't understand.")
