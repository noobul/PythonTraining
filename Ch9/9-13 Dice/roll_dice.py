import dice

default_dice = dice.Dice()
ten_dice = dice.Dice(10)
twenty_dice = dice.Dice(20)

default_dice.roll_dice(10)
print('-------------------')
ten_dice.roll_dice(10)
print('-------------------')
twenty_dice.roll_dice(10)
print('-------------------')