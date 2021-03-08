#7-1 Rental car
car = input("What kind of car would you like: ")
print(f"Let me see if I can find a {car.title()}")

#7-2 REstaurant sitting
party = input("How many people are in your party?: ")
party = int(party)

if party > 8:
    print("Please wait untill a table is free.")
else:
    print("Please follow me to your table.")

#7-3 multiple of ten
prompt = "Is this a multiple of 10?"
prompt += "\nEnter number: "
number = input(prompt)
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} number is not a multiple of 10.")