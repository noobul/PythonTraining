import json_handler_class

user_add = "You have been added successfully:"
user_display = "You're: "
ask_prompt = "Is the curren username correct? (type 'y' or 'n')"
prompt = "Enter username:  "
file_name = "Ch10/10-11-12/user.json"

user = json_handler_class.JasonHandler(file_name)
try:
    user.read_from_json(user_display)
    ask = input(ask_prompt)
    if ask == 'n':
        user.add_to_json(prompt, user_add)
    elif ask == 'y':
        print("Awesome!")
    else:
        print('Wrong input')
        pass
except FileNotFoundError:
    user.add_to_json(prompt, user_add)
