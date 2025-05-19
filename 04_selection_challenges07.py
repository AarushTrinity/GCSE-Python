#Ask the user to enter a number
number = int(input("Please enter a number"))
# If it is under 10, display the message "too low"
if number < 10:
    print("too low")
#If the number is between 10 and 20, display "correct"
elif 10 < number <= 20:
    print("correct")
#Otherwise, display "too high you crazy pizza pie"
else:
    print("too high you crazy pizza pie")
