import random
import art
from os import system
from ProjectData import data
def generate_account():
# generate data to compare
    '''this function generate data of a member for comparision'''
    return random.choice(data)
def compare(a,b):
    # comparision of the two..
    '''this function compare the followers of two people present in the data'''
    if a['follower_count']>b['follower_count']:
        return "A"
    else:
        return "B"

def game():
    print(art.logo)
    game_continue = True
    current_score = 0
    while game_continue:
        a = generate_account()
        b = generate_account()
        # print the data
        print(f"compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(art.vs)
        print(f"compare B: {b['name']}, a {b['description']}, from {b['country']}")
        highest_followers = compare(a,b)
        highest_followers_by_user = input("who has more followers? (A/B)  ").upper()

        if highest_followers_by_user == highest_followers:
            current_score+=1
            system("cls")
            print(art.logo)
            print(f"Right answer, your score is {current_score}\n")
            a = generate_account()
            b = generate_account()
        else:
            system("cls")
            print(f"you loose!, your score is {current_score}")
            game_continue = False
game()