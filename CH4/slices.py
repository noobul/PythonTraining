#4-10
foods = ["pizza", "falafel","shaworma", "carrot cake", "cannoli", "ice cream"]
first_slice = foods[:3] #prints first 3
second_slice = foods[1:4] #definde slice
last_slice = foods[-3:] #prints last 3
print(first_slice)
print(second_slice)
print(last_slice)
for food in foods:
    print(food)

#4-11

pizzas = ["Picante", "Vegetarian", "Margherita"]
fried_pizzas = pizzas[:]
pizzas.append("Quatro stagioni")
fried_pizzas.append("Quatro carne")
print(pizzas)
for pizza in pizzas:
    print(pizza)
print(fried_pizzas)