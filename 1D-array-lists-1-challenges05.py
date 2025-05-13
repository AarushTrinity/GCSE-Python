food = []

for i in range(4):
    food1 = str(input("Enter one type of food (this will be asked 4 times): "))
    food.append(food1)

print(food)

item = int(input("Enter number of item to delete>>> "))
item = item-1

del food[item]
print(food)
