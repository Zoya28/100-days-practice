from random import randint
logo = '''                                         
                            (_)                                         
   __ _ _   _  ___  ___ ___ _ _ __   __ _    __ _  __ _ _ __ ___   ___ 
  / _` | | | |/ _ \/ __/ __| | '_ \ / _` |  / _` |/ _` | '_ ` _ \ / _ \
 | (_| | |_| |  __/\__ \__ \ | | | | (_| | | (_| | (_| | | | | | |  __/
  \__, |\__,_|\___||___/___/_|_| |_|\__, |  \__, |\__,_|_| |_| |_|\___|
   __/ |                             __/ |   __/ |                     
  |___/                             |___/   |___/                      
  
'''
def difficulty_level():
    difficulty = input("choose difficulty, hard or easy : ")
    if difficulty == "easy":
        return 10
    else:
        return 5
def check_answer(comp,guess):
    if guess < comp:
        print("too low..")
        print("guess again..")
        return 1
    elif guess > comp:
        print("too high..")
        print("guess again..")
        return 1
    else:
        print(f"you guessed correct. the answer is {comp}\n")
        return 0
def game():
    print(logo)
    print("welcome to the Number guessing game! ")
    print("I am thinking of a number between 1 and 100")
    computer_guess = randint(1,100)
    print(f"the number is {computer_guess}")
    attempts = difficulty_level()
    while attempts != 0:
        print(f"\nyou have {attempts} attempts left.")
        guess = int(input("make a guess: "))
        answer = check_answer(computer_guess,guess)
        if answer == 0:
            break
        attempts-=1
    if answer != 0 :
        print("you ran out of guesses. you loose!\n")
game()