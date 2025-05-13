party_guest_list = []
name = input("Input the names of three people you would like to invite to the party.")
for i in range(3):
    party_guest_list.append(name)
    
while True:
    question_another_name = input("Would you like to add another name?")
    
    if question_another_name == 'yes':
        another_name = input("What is the name that you would like to add?")
        party_guest_list.append(another_name)
    elif question_another_name == 'no':
        print(len(party_guest_list))
        break
        
