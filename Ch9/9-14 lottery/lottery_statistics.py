import lottery

my_ticket = [1, 8, 'a', 'c']
nr_runs = 0

play_lottery = lottery.Lottery()

test = True
while test:
    result = set(play_lottery.play())
    my_ticket = set(my_ticket)
    print(result)
    nr_runs += 1
    if result == my_ticket:
        break

print(nr_runs)
print(f"{result} and {my_ticket}")