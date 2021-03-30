filename = 'test.txt'

file_lines = []

with open(filename) as file_object:
    #prints entire file
    content = file_object.read()
    print(content.rstrip())

    #prints file content line by line
    for line in file_object:
        print(line.rstrip())
    
    #store data from file in file_lines lsit
    for line in file_object:
        file_lines.append(file_object)

for file_line in file_lines:
    print(file_line)
