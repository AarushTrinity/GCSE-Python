#Ask a user to enter a number below 50
num = int(input("Please enter a number below 50: "))

start_num = 50
#Then countdown from 50 to that number
for i in range(start_num, num - 1, -1):
    print(i)
#Shows the number that they entered in the output
print("The number you entered was:", num)
