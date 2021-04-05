filename = "Ch10/10-1/test.txt"

file_lines = []

with open(filename) as file_object:
    #prints entire file
    content = file_object.read()
    print(content.rstrip())

with open(filename) as file_object:
    #prints file content line by line
    for line in file_object:
        print(line.rstrip())
    
with open(filename) as file_object:
    #store data from file in file_lines lsit
    for line in file_object:
        file_lines.append(line)

#prints each line in list
for file_line in file_lines:
    print(file_line.strip())

#replace 'Pyhton' with 'C#' for each line in the list durring print
for file_line in file_lines:
    print(file_line.replace('Python', 'C#').strip())