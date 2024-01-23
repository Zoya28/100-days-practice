import random
import os
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_cards():
    total_card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    cards = random.choice(total_card)
    return cards
def total_score(card):
    '''take a list of the cards and calculate the total score from the card'''
    score = sum(card)
    if score == 21 and len(card) == 2:
        return 0
    if 11 in card and score > 21:
        card.remove(11)
        card.append(1)
    return score
def compare (user_score,computer_score):
    if computer_score == user_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "you loose!"
    elif user_score == 0:
        return "you won!"
    elif user_score > 21:
        return "you lost!"
    elif computer_score > 21:
        return "You won!"
    elif user_score > computer_score:
        return "you won!"
    else:
        return "you loose!"
def black_jack():
    print(logo)
    user_card = []
    computer_card = []
    game_over = False

    for _ in range(2):
        user_card.append(deal_cards())
        computer_card.append(deal_cards())

    while not game_over:     
        user_score = total_score(card=user_card)
        computer_score = total_score(card=computer_card)
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"computer's first card: {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            continue_game = input("\nType 'y' to draw another card. type 'n' to end the game. ")
            if continue_game == 'y':
                user_card.append(deal_cards())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_cards())
        computer_score = total_score(computer_card)

    print(f"\nyour final hand : {user_card}, your final score : {user_score}")
    print(f"computer's final hand : {computer_card}, computer's final score :{computer_score}\n")
    print(compare(user_score , computer_score))
    restart = input("\nDo you want to restart the game? (y/n) ")
    if restart == "y":
        os.system("cls")
        black_jack()
black_jack()