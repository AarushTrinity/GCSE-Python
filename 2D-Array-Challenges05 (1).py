EmptyArray = [["a" for column in range(5)] for row in range(10)]
print(EmptyArray)
range_value  = int(input("please enter the range of lists >>> "))
range_values  = int(input("please enter the amount of times you want repeat 'a' in a list >>> "))
EmptyArray = [["a" for column in range(range_values)] for row in range(range_value)]
print(EmptyArray)
