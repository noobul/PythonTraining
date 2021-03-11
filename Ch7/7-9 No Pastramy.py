sandwich_orders = ['BLT', 'Pastrami', 'Tuna', 'Veggie', 'Pastrami', 'chicken salad', 'Pastrami', 'Italian BMT']
finished_sandwiches = []

print('We are out of Pastrami!')

while sandwich_orders:    
    while 'Pastrami' in sandwich_orders:
        sandwich_orders.remove('Pastrami')

    sandwich_order = sandwich_orders.pop()

    print(f"Your {sandwich_order} sandwich is finished.")
    finished_sandwiches.append(sandwich_order)