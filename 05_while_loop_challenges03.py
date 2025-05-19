# Ask the user to enter a number
num = int(input("Enter a number: "))

# Outside the loop, create a variable that holds the first number
first_num = num

# Outside the loop create a variable that stores the number entered in the step above
# into a variable called "total"
total = num

# Outside the loop, create a variable that holds the value "y"
add_more = "y"

# Inside the loop, ask to enter another number
while add_more.lower() == "y":
    num = int(input("Enter another number: "))

    # Add the two numbers together
    total += num

    # Ask if they want to add another number
    add_more = input("Do you want to add another number? (y/n): ")

# Once the loop has stopped, display the total
print("The total is:", total)
