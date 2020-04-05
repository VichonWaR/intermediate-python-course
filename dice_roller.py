import random

def main():
    dice_rolls = int(input("How many dice would you like to roll? "))
    dice_sum = 0
    dice_size = int(input('How many sides are on the dice? '))
    
    for i in range(0,dice_rolls):
        roll = random.randint(1,dice_size)
        dice_sum += roll
        print(f'You rolled a {roll}')
    if dice_sum - roll == roll:
        print('Doubles!')
    print(f'A total of {dice_sum}')
    input('Press ENTER to exit!')

if __name__== "__main__":
  main()