#6-1 Person
person_0 = {
    "first_name": "Doe",
    "last_name": "John",
    "age": "25",
    "city": "New York",
}
print(person_0)

#6-2 Favourite numbers
favourite_numbers = {
    "John" : "5",
    "Maria": "1",
    "Leonard": "7",
    "Jimmy": "9",
    "Anna": "3",
}
for favourite_number in favourite_numbers:
    name = favourite_numbers[f'{favourite_number}']
    print(f"{favourite_number}: {name}")

#6-3 Glossary
programming_words = {
    "variable" : "keyword that can store data",
    "string" : "text data type",
    "boolean" : "data type that can have the value 'true' and 'false'",
    "if-else condition" : "method for checking conditions and executing code based on result",
    "integer" : "whole-number data type",
}

for programming_word in programming_words:
    definition = programming_words[f'{programming_word}']
    print(f"The {programming_word} is a {definition}.")