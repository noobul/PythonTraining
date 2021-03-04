#6-7 People
person_0 = {
    "first_name": "Doe",
    "last_name": "John",
    "age": "25",
    "city": "New York",
}
person_1 = {
    "first_name": "Forman",
    "last_name": "Red",
    "age": "55",
    "city": "Point Place",
}
person_2 = {
    "first_name": "Dorian",
    "last_name": "John",
    "age": "30",
    "city": "Los Angeles",
}

people = (person_0, person_1, person_2)

for person in people:
    print(person)

#6-9 favorite places
favorite_places = {
    "John" : ["CoffeBucks"],
    "Red" : ["The Lake", "The Couch"],
    "Maria" : ["The Mall", "Paris", "CoffeBucks"],
}

for person, places in favorite_places.items():
    if len(places) > 1:
        print(f"{person}, your favorite places are:")
    else:
        print(f"{person}, your favourite place is:")
    for place in places:
       print(f"\t{place.title()}")

#6-10 favorite numbers
favourite_numbers = {
    "John" : ["5", "12"],
    "Maria": ["1", "2", "3"],
    "Leonard": ["7"],
    "Jimmy": ["9", "5"],
    "Anna": ["3"],
}

for person, numbers in favourite_numbers.items():
    if len(numbers) > 1:
        print(f"{person}, your favourite numbers are: ")
    else:
        print(f"{person}, your favourite number is: ")
    for number in numbers:
        print(f"{number}")

#6-11 Cities
cities = {
    'Cluj-Napoca':{
        'county' : 'Cluj',
        'population' : '321687',
        'fact' : "In German it's called 'Klausenburg'",
    },
    'Bucuresti' : {
        'county' : 'n/a',
        'population' : '2151655',
        'fact' : "It's the capital of Romania",
    },
    'Brasov' : {
        'county' : 'Brasov',
        'population' : '290743',
        'fact' : "The 'Black Church' is situated here.",
    }
}

for city, details in cities.items():
    print(f"{city}:")
    for detail, info in details.items():
        print(f"\t{detail} : {info}")