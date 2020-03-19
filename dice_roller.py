import random

def main():
    dice_rolls = int(input("How many dice would you like to roll? "))
    dice_sum = 0
    for i in range(0,dice_rolls):
        roll = random.randint(1,6)
        dice_sum += roll
        print(f'You rolled a {roll}')
    if dice_sum - roll == roll:
        print('Doubles!')
    print(f'A total of {dice_sum}')

if __name__== "__main__":
  main()