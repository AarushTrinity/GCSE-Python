#Ask the user to  enter a number between 10 and 20
number = int(input("Please enter a number between 10 and 20"))

#If they enter a number that is between 10 and 20, display the message "Thank you"
if 10 <= number <=20:
    print("Thank you")

#If the number is less than 10, then it will display the message "Incorrect answer"

elif number <  10:
    print("Incorrect answer")
