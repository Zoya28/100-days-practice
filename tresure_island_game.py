print('''....welcome to the treasure island game....
    your mission is to find the treasure.''')

choice1 = input("you are at the cross road. where do you wanna go? 'Right' or 'Left'\n").lower()
if choice1 == "right":
    choice2 = input("you have come to a lake. what do you wanna do? wait or swim.\n").lower()
    if choice2 == "swim":
        choice4 = input("you have arrived to the island. there are 3 doors 'Red' , 'yellow' , 'Green'? which one will you choose?\n").lower()
        if choice4 == 'red':
            print("congratuations.....you got the treasure.")
        elif choice4 == "yellow":
            print("you are trapped. game is over....")
        else:
            print("you are dead, game is over.....")
    else:
        choice8 = input("the boat you got is damadged. there is another way which go to the forest. do you wanna 'go' or 'swim'?\n").lower()
        if choice8 == "swim":
            choice9 = input("you have arrived to the island. there are 3 doors 'Red' , 'yellow' , 'Green'? which one will you choose?\n").lower()
            if choice9 == 'red':
                print("congratuations.....you got the treasure.")
            elif choice9 == "yellow":
                print("you are trapped. game is over....")
            else:
                print("you are dead, game is over.....")
        else:
            print("you are dead in the forest. GAME OVER...")
else:
    choice3 = input("you have come to a building and there are weapons. what do you wanna do? do you want to take it or not? y/n\n").lower()
    if choice3 == "n":
        choice5 = input("now you've got 2 ways. first will take you to the lake and 2nd one will get you to the forest. what do you wanna do? go to the 'lake' or 'forest'\n").lower()
        if choice5 == 'lake':
            choice6 = input("you have come to a lake. what do you wanna do? wait or swim.\n").lower()
            if choice6 == "swim":
                choice7 = input("you have arrived to the island. there are 3 doors 'Red' , 'yellow' , 'Green'? which one will you choose?\n").lower()
                if choice7 == 'red':
                    print("congratuations.....you got the treasure.")
                elif choice7 == "yellow":
                    print("you are trapped. game is over....")
                else:
                    print("you are dead, game is over.....")
            else:
                choice11=("the boat you got is damadged. there is another way which go to the forest. do you wanna 'go' or 'swim'?")
                if choice6 == "swim":
                    choice10 = input("you have arrived to the island. there are 3 doors 'Red' , 'yellow' , 'Green'? which one will you choose?\n").lower()
                    if choice10 == 'red':
                        print("congratuations.....you got the treasure.")
                    elif choice10 == "yellow":
                        print("you are trapped. game is over....")
                    else:
                        print("you are dead, game is over.....")
                else:
                    print("you are dead in the forest. GAME OVER...")
        else:
            print("you are dead in the forest. GAME OVER...")
    else:
        print('''you steppend on the bomb in 3 seconds you will be dead...GAME OVER...''')