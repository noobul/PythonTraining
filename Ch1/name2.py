input_first_name = " Blake"
input_middle_name = " hellbalzer "
input_last_name = "john "
salutations = "Hello!"
message = "How are you today?"
first_name = f"{input_first_name.lstrip()}"
middle_name = f"{input_middle_name.strip().title()}"
last_name = f"{input_last_name.rstrip().title()}"
name = f'{first_name} "{middle_name}" {last_name}'
display_message = f"\t\t{salutations} \n\t{name} \n\t{message}"
print(display_message)