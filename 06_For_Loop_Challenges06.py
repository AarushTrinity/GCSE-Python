# Initialize the variable total to 0
total = 0

# Use a for loop to ask the user for five numbers
for i in range(5):
    # Ask the user to enter a number
    num = int(input("Enter a number: "))

    # Ask the user if they want to include the number
    include = input("Do you want to include this number? (y/n): ")

    # If the user says yes, add the number to the total
    if include == "y":
        total += num

# Print the final total
print("The total is:", total)
