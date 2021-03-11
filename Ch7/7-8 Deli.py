sandwich_orders = ['BLT', 'Tuna', 'Veggie', 'chicken salad', 'Italian BMT']
finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()

    print(f"Your {sandwich_order} sandwich is finished.")
    finished_sandwiches.append(sandwich_order)