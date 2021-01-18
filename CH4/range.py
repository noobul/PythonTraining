#4-3
for value in range(1, 21):
    print(value)

#4-4
milion = [range(1, 1000001)]
#4-5
print(min(milion))
print(max(milion))

#for value in milion:
    #print(value)

#4-6
for value in range(1, 21, 2):
    print(value)

#4-7
for value in range(3, 31, 3):
    print(value)

#4-8
cubes = []
for value in range(1, 11):
    cube = value**3
    cubes.append(cube)
print(cubes)

#4-9
cubes = [value**3 for value in range(1,11)]
print(cubes)