dream_vacation = {}

dreams = True

while dreams:
    who_are_you = 'Please enter your name: '
    name = input(who_are_you)
    destination_promot = f'{name.title()}, if you could visit only one place, where would you go? '
    destination = input(destination_promot)

    dream_vacation[name] = destination

    repeat = input("Would someone else like to respond? (yes/no)")
    if repeat == 'no':
        dreams = False
    elif repeat == 'yes':
        dreams = True
    else:
        print("Invalid input")
        dreams = False
        
print('---poll results!---')
for name, destination in dream_vacation.items():
    print(f'{name} would like to visit {destination}')