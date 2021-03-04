#6-4 Glossary 2
programming_words = {
    "variable" : "keyword that can store data",
    "string" : "text data type",
    "boolean" : "data type that can have the value 'true' and 'false'",
    "if-else condition" : "method for checking conditions and executing code based on result",
    "integer" : "whole-number data type",
}

for variable, definition in programming_words.items():
    print(f"The {variable} is a {definition}")

#6-5 Rivers
major_rivers = {
    'nile' : 'egypt',
    'danube' : 'romania',
    'amazon' : 'brazil',
}

for river, country in major_rivers.items():
    print(f"The {river.title()} runs through {country.title()}")
for river1 in major_rivers.keys():
    print(river1)
for country1 in major_rivers.values():
    print(country1)

#6-6 Polling
favourite_languages = {
    'jen' : 'python',
    'sarah' : 'C',
    'edward' : 'ruby',
    'phil' : 'python',
}

people_to_thake_the_poll = ('jen', 'phil', 'matt',  'maria')

for person in favourite_languages:
    if person in people_to_thake_the_poll:
        print(f"Thank you, {person.title()}, for taking the poll.")
    else:
        print(f"{person.title()}! Please take the poll.")