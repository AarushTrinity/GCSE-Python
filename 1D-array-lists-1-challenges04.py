TV_programmes = ['Cobra Kai', 'The Big Bang Theory', 'Friends', 'Invincibles',]

print(TV_programmes[0])
print(TV_programmes[1])
print(TV_programmes[2])
print(TV_programmes[3])

Show1 = str(input("Enter a show "))
Position = int(input("Enter position "))
Position = Position - 1
TV_programmes.insert(Position,Show1)
print(TV_programmes)