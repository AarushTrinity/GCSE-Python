counter = 1  # Start with 1 for the unique number

while True:  # Keep looping until we break out
    last_name = input("Enter a last name (or type 'quit' to stop): ")

    if last_name.lower() == "quit":  # Check if the user wants to stop
        break  # Exit the loop

    first_three = last_name[:3]  # Get the first three letters
    membership_number = first_three + str(counter)  # Combine letters and number

    print("Membership number:", membership_number)
    counter += 1  # Increase the counter for the next name
