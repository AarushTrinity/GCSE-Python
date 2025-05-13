cars = []

while True:
    choice = input("input a car brand or press x to exit ")
    
    if choice == 'x':
        print("exiting...")
        print(cars) 
        break
    else:
        cars.append(choice)