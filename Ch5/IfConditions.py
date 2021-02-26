#AlienColours1
alien_color = 'green' 
alien_color1 = "blue"
if alien_color == 'green':
    print('You get 5 points')
if alien_color == 'red':
    print()

#AlienColours2
if alien_color == 'green':
    points = 5
else:
    points = 10
print(f"you got {points} points")

if alien_color1 == 'green':
    points = 5
else:
    points = 10
print(f"you got {points} points")

#AlienColor3
aliens = ("green", "yellow", "red")
for alien in aliens:
    if alien == "green":
        points = 5
    if alien == "yellow":
        points = 10
    if alien == "red":
        points = 15
    print(f"You got {points} points for killing {alien} alien")

#Stages of life
age = 18

if age < 2:
    stage = 'a baby'
elif age < 4:
    stage = 'a toddler';
elif age < 13:
    stage = 'a kid'
elif age < 20:
    stage = 'a teenager'
elif age < 65:
    stage = 'an adult'
else:
    stage = 'an elder'

print(f"That person is {stage}")

#favorite fruit
favorite_fruits = ('apple', 'bannana', 'avocado')

for fruit in favorite_fruits:
    if fruit == 'bannana':
        print(f"He must really like {fruit}")
for fruit in favorite_fruits:
    if fruit == 'apple':
        print(f"He must really like {fruit}")
for fruit in favorite_fruits:
    if fruit == 'avocado':
        print(f"He must really like {fruit}")
for fruit in favorite_fruits:
    if fruit == 'orange':
        print(f"He must really like {fruit}")
for fruit in favorite_fruits:
    if fruit == 'tomato':
        print(f"He must really like {fruit}")
