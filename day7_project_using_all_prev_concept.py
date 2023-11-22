import random
print('''
                --------This is Hangman game!-----------
*********************************************************************************

--->  You will get 7 lives to complete this game.
--->  If you guess a wrong character, 1 letter from word "HANGMAN" will be vanished.
--->  If all the letter is vanished, you will loose the game.

Hint: It is a bollywood movie of year 2021

*********************************************************************************
''')
word_list=["Shershaah","Mimi","Antim","Dhamaka","Kaagaz","Sherni","Pagglait","Tribhanga","Chehre"]
choosen_word=random.choice(word_list).lower()
# print(f"the solution is {choosen_word}")
lives_list=["H","A","N","G","M","A","N"]
display=[]
for each in choosen_word:
    display.append("_")
end_of_game = False
print("H A N G M A N")
while not end_of_game:
    guess=input("\nchoose a letter from a-z: ").lower()
    for position in range(len(choosen_word)):
        if guess==choosen_word[position]:
            display[position]=guess
        else:
            continue
    if guess not in choosen_word:
        life=""
        print(f"\nyou guessed {guess}, thats not in the word, you loose a life...")
        lives_list.pop()
        for number in lives_list:
            life=life+" "+number
        print(life,"\n")
    for items in display:
        print(items,end=" ")
    if "_" not in display or not lives_list:
        end_of_game=True
        if "_" not in display:
            print("\nyou won!!")
        else:
            print("\nyou loose!!")
            print(f"correct movie name was {choosen_word} !\n\n")



