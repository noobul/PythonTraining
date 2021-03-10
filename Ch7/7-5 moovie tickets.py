price_3 = '$0'
price_3_12 = '$10'
price_12 = '$15'

prompt = 'Would you like to see a movie?'
prompt += '\nPlease submit the age to check the price: '

loop = True

while loop:
    age_input = input(prompt)
    age = int(age_input)

    if age <= 3:
        print(f'The price is {price_3}')
        continue
    if age <= 12:
        print(f'The price is {price_3_12}')
        continue
    if age > 12:
        print(f'The price is {price_12}') 
        continue
    else:
        loop = False