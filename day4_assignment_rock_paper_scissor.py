import random as rd

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
            ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


game_choice = [rock, paper, scissors]
choice = int(input("what do you choose? choose 0 for rock, 1 for paper and 2 for scissor.\n"))
if choice >= 3 or choice < 0:
    print("invalid input..")
else:
    print(game_choice[choice])
    rand_number = rd.randint(0,2)
    print("computer choose:",game_choice[rand_number])
    
    
    if choice == rand_number:
        print("it's a draw...")
    elif choice==2 and rand_number == 0:
        print("you loose...")
    elif rand_number==2 and choice == 0:
        print("you won...")
    elif choice < rand_number:
        print("you loose..")
    elif choice > rand_number:
        print("you win..")
