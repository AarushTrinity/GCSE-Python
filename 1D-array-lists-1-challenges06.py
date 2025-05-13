nums = []

for i in range(3):
    num = int(input("Please enter a number"))
    nums.append(num)
last_num = str(input("Would you like to save the last number you entered? "))
if last_num == "yes":
    print(nums)
elif last_num == "no":
    num = 3
    num = num-1
    del nums[num]
    print(nums)