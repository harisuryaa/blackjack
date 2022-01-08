
from art import logo
import random
from replit import clear

def sum_cards(c1):
    if sum(c1)== 21 and len(c1)==2:
        return 0
    if 11 in c1 and sum(c1) > 21:
        c1.remove(11)
        c1.append(1)
    return sum(c1)
    
def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    
    
    condition = input("Press 'y' to pick a card or 'n': ")
  
    if condition == "y":
        set_begining = True
    elif condition == "n":
        set_begining = False
    else:
        print("enter a vaild key")
    user_card=[]
    computer_card=[]
    
    def card_picker(cards):
        return random.choice(cards)
    
    def compare(user, sys):
        c1 = sum_cards(user)
        c2= sum_cards(sys)
        if c1 > c2 and c1 < 21:
            print("You win :) ")
    
        elif c2 > c1 and c2 < 21:
            print("you Loose :( ")
            
        elif c1 == c2 or c1== 21 or c2== 21:
            print("draw")
    
    while set_begining:
        print(logo)
        if sum_cards(user_card)==0:
            for x in range(2):
                user_card.append(card_picker(cards))
        if sum_cards(computer_card)==0:
            for x in range(2):
                computer_card.append(card_picker(cards))
        else:
            user_card.append(card_picker(cards))
            computer_card.append(card_picker(cards))
        user_score=sum_cards(user_card)
        computer_score=sum_cards(computer_card)
        
        print(f"{user_card} = scores are {user_score}")
        print(f"computer's card {computer_card[0]}")
        # print(f"computer's card {computer_card} = score {computer_score}")
        if user_score > 21:
            print(f"your score is above 21 ")
            print("You Loose :( ")
            set_begining = False    
        if set_begining:
            check = input("do u want to check 'y' or 'n' to pick card ")
            if check != "y" and check != "n":
                print("invalid key")
                return
            if check == "y":
                print(f"ur score {user_score} computer score {computer_score}")
                compare(user_card, computer_card)
            print(f"ur score {user_score} computer score {computer_score}")
            compare(user_card, computer_card)    
            condition = input("Do you want to play blackjack again 'y' or 'n': ")
            if condition != "y" and condition != "n":
                print("invalid key")
                return
            
            if condition == "y":
                set_begining = True
                clear()
                blackjack()
            elif condition == "n":
                set_begining = False
        clear()

    
    


blackjack()








