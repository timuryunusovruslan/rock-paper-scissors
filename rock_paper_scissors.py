import random 

print("1 - rock, 2 - scissors, 3 - paper")

player_choice = int(input("Choose 1, 2 or 3: "))

print(f"You have choosen {player_choice}")

computer_choice = random.randint(1, 3)

if player_choice == 1 and computer_choice == 3:
    print("computer has choosen paper : computer won!")
elif player_choice == 2 and computer_choice == 1:
    print("computer has choosen rock : computer won!")
elif player_choice == 3 and computer_choice == 2:
    print("computer has choosen scissors : computer won!")
elif player_choice == 1 and computer_choice == 2:
    print("computer has choosen scissors : player won!")
elif player_choice == 2 and computer_choice == 3:
    print("computer has choosen paper : player won!")
elif player_choice == 3 and computer_choice == 1:
    print("computer has choosen rock : player won!")
else:
    print("It's a draw!")


