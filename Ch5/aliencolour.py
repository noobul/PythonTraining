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