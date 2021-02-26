#5-8 and 5-9
usernames = ('admin', 'johm', 'kitty55', 'vasile69', 'belzebub')
if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"Hello {user}. Would you like to see a status report?")
        else:
            print(f"Jello {user}, thank you for logging in again.")
else:
    print("We need to add some users.")

#5-10 Checking usernames
current_users = ('johm', 'kitty55', 'vasile69', 'Belzebub', 'Bro')
new_users = ('ale73', 'panda', 'Bro', 'VASILE69', 'GutzaRULLZ')
current_users_lower = []

for current_user in current_users:
    current_user_lower = current_user.lower()
    current_users_lower.append(current_user_lower)

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The {new_user} username is invalid")
    else:
        print(f"The {new_user} usename is valid")

#5-11 Ordinal numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")