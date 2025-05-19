EmptyArray = [["a" for column in range(5)] for row in range(10)]
print(EmptyArray)
range_value = int(input("please enter the range value >>> "))
EmptyArray = [["a" for column in range(range_value)] for row in range(range_value)]
print(EmptyArray)
