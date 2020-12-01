first_name = "ada "
last_name = " lovelace"
#rstrip() - removes white space from right side of string
#lstrip() - removes white space from left side of string
#strip() - removes white space from both sides of string
full_name = f"{first_name.rstrip()} {last_name.lstrip()}"
print(full_name.title())
print(full_name.upper())
print(full_name.lower())
message = (f"Hello, {full_name.title()}!")
print(message)