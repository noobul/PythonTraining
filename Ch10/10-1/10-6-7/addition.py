def add_method(fst_number, snd_number):
    try:
        result = int(fst_number) + int(snd_number)
    except ValueError:
        print("You didn't enter a number")
    else:
        print(result)

while True:
    first_number = input("Please enter a number: ")
    if first_number == 'q':
        break
    second_number = input("Please enter a second number: ")
    if second_number == 'q':
        break
    add_method(first_number, second_number)