def invite_people():
  #Asks the user how many people they want to invite to a party, and then asks for the names of each person if the number is less than 10.

  while True:  # Keep asking until a valid number is entered
    try:
      num_people = int(input("How many people do you want to invite to the party? "))
      break  # Exit the loop if a valid number is entered
    except ValueError:
      print("Invalid input. Please enter a whole number.")

  if num_people < 10:
    for i in range(num_people):
      name = input(f"Enter the name of person {i+1}: ")
      print(f"{name} has been invited!")
  else:
    print("That's too many people for a party! Let's keep it under 10.")

# Start the process
invite_people()
