import random

computer_choice = random.choice(["Rock", "Paper", "Scissors"])
user_choice = input("Enter your choice : ")

print("Computer choice is :",computer_choice)

if user_choice == computer_choice :
    print("It's a TIE !!")
elif user_choice == 'Paper' and computer_choice == 'Rock' :
    print("You WIN !!")
elif user_choice == 'Paper' and computer_choice == 'Scissors' :
    print("You LOSE !!")
elif user_choice == 'Rock' and computer_choice == 'Paper' :
    print("You LOSE !!") 
elif user_choice == 'Rock' and computer_choice == 'Scissors' :
    print("You LOSE !!") 
elif user_choice == 'Scissors' and computer_choice == 'Paper' :
    print("You LOSE !!") 
elif user_choice == 'Scissors' and computer_choice == 'Scissors' :
    print("You LOSE !!")    
else : #user_choice == 'Scissors' :
    print("You LOSE !!")
