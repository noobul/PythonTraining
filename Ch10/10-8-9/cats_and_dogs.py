cats = 'Ch10/10-8-9/cats.txt'
dogs = 'Ch10/10-8-9/dogs.txt'

def read_file(file_object):
    try:
        with open(file_object) as f:
            for line in f:
                print(line.rstrip())
    except FileNotFoundError:
        pass

read_file(cats)
print(" ")
read_file(dogs)