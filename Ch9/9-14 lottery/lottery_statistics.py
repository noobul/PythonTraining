import lottery

my_ticket = [1, 8, 'a', 'c']
nr_runs = 0

play_lottery = lottery.Lottery()

result = play_lottery.play().sort()

while my_ticket != result:
    nr_runs +=1
print(nr_runs)