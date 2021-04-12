import json_handler_class

number_add = "We'll that your favorinte number is:"
number_display = "Your favorinte number is:"
prompt = "What is your favorite number? "
file_name = "Ch10/10-11-12/fav_number.json"

fav_nr = json_handler_class.JasonHandler(file_name)
try:
    fav_nr.read_from_json(number_display)
except FileNotFoundError:
    fav_nr.add_to_json(prompt,number_add)
