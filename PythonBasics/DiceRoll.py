import random

dice_value = random.randint(1,6)

user_guess = int(input("Guess the number for the dice roll :"))

print("The value of dice roll is", dice_value)

if user_guess == dice_value :
    print("Yay, you are the winner!")
else :
    print("Nay, you are the loser!")