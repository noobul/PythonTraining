loop = True
toppings = []

while loop:
    prompt = 'What would you like on your pizza?'
    prompt += '\nType quit to exit, type selection to see current toppings, type order to submit: '
    topping = input(prompt)  
    toppings_prompt = f"The {topping} has been added to the list."
    selection = f"This is your current selection{toppings}"
    if topping == 'quit':
        loop = False
    elif topping == 'selection':
        print(selection)
    elif topping == 'order':
        print('Your order has been submited.')
        loop = False
    else:
        toppings.append(topping)
        print(toppings_prompt)