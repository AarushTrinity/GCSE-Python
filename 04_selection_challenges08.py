#Ask the user to enter a number 1,2 or 3
number = int(input("Please enter a number 1,2,or 3"))
#If they enter 1, display the message "thank you"
if number == 1:
    print("thank you")
#If they enter 2, display the message "well done, you're so smart"
elif number == 2:
    print("well done, you're so smart")
#If they enter 3, display the message "amazing,you are so good at this"
elif number == 3:
    print("amazing,you are so good at this")
#If they enter anything else, display the message "really?What is wrong with you??"
else:
    print("really?What is wrong with you??")
