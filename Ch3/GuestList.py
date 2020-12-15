#Exercisse 3-4
people = ["Hendrix", "Page", "Freddy"]
print(f"{people} are invited to dinner")

#Exercise 3-5
cant_makeit = people.pop(2)
print (f"{cant_makeit} can't make it")
people.append("Cobain")
print(f"{people} are invited to dinner")

#Exercise 3-6
print("I found a bigger table")
people.insert(0, "Einstein")
people.insert(2, "Hitler")
people.append("Stalin")
print(f"{people[0]} you're invited to dinner")
print(f"{people[1]} you're invited to dinner")
print(f"{people[2]} you're invited to dinner")
print(f"{people[3]} you're invited to dinner")
print(f"{people[4]} you're invited to dinner")
print(f"{people[5]} you're invited to dinner")

#Exercise 3-7
print("I can only invite two people for dinner")
print(f"{people.pop()} you're uninvited")
print(f"{people.pop()} you're uninvited")
print(f"{people.pop()} you're uninvited")
print(f"{people.pop()} you're uninvited")

print(f"{people[0]} you're still invited to dinner")
print(f"{people[1]} you're still invited to dinner")

#3-9
list_len = len(people)
print(list_len)

del people[1]
del people[0]

print(people)

#3-9
list_len = len(people)
print(list_len)