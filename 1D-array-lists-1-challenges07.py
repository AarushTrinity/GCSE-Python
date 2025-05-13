def modify_array():
    number_list = [10, 25, 30, 45, 50]
    print("Original List:", number_list)
    position_to_change = int(input("Enter the position you want to change (1 to 5): ")) - 1
    new_number = int(input("Enter the new number: "))
    number_list[position_to_change] = new_number
    print("Updated List:", number_list)

modify_array()
