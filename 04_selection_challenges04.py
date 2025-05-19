#Ask user to enter their favourite colour
fav_colour = input("What is your favourite colour?")
#If they enter "red" or "RED" or "Red", then it will display the message "I like red too"
if fav_colour == "red" or "RED" or "Red":
    print("I like red too")
#Otherwise it will display the message "I don't like {colour},{colour} is for losers"
else:
    print("I don't like", fav_colour, ". ", fav_colour, "is for losers.")
