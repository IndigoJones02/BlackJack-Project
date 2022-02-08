# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from random import randint

# Write all of your code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
player_turn = 0 
answer = ""
value = 0
player_0 = 0
player_1 = 0

while player_turn < 2:
     if player_turn == 0:
         print("-----------")
         print("YOUR TURN")
         print("-----------")
     elif player_turn == 1: 
         print("-----------")
         print("DEALER TURN")
         print("-----------")
  
     card_pulled = 0 
  
     while card_pulled < 2:
         card = randint(1, 13)
         if card == 1:
             print("Drew a Ace")
         elif card == 11:
             print("Drew a Jack")
         elif card == 12:
             print("Drew a Queen")
         elif card == 13: 
             print("Drew a King")
         else:
             print("Drew a "+str(card))

         card_value = 0
  
         if card == 1:
             card_value = 11
         elif card >= 11 and card <= 13:
             card_value = 10
         else:
             card_value = card
    
         value = value + card_value
         card_pulled = card_pulled + 1
   
     if not value >= 21 and player_turn == 0:
         answer = input("You have "+ str(value) +". Hit (y/n)? ")
         if answer == "n" or answer == " n":
             print("Final hand: "+str(value) + ".")
             player_0 = value
     elif not value >= 21 and player_turn == 1 and not value in range(18, 21):
         print("Dealer has " + str(value) + ".")

     while (value < 21 and not value >= 21 and player_turn == 0 and (answer == "y" or answer == " y")) or (value <= 17 and player_turn == 1): 
         if (answer == "y" or answer == " y") or player_turn == 1:
             card3 = randint(1, 13)
         if card3 == 1: 
             print("Drew a Ace")
         elif card3 == 11: 
             print("Drew a Jack")
         elif card3 == 12:
             print("Drew a Queen")
         elif card3 == 13:
             print("Drew a King")
         else:
             print("Drew a "+str(card3))
         card3_value = card3
         if card3 == 1:
             card3_value = 11
         elif card3 >= 11 and card3 <= 13: 
             card3_value = 10
         else: 
             card3_value = card3 
         value = value + card3_value
         if not value in range(18, 21) and not value >= 21 and player_turn == 1: 
             print("Dealer has " + str(value) + ".")
         elif not value >= 21 and player_turn == 0:
             answer = input("You have "+ str(value) +". Hit (y/n)? ")
             if answer == "n" or answer == " n":
                 print("Final hand: " + str(value) + ".")
                 player_0 = value

     if value in range(18, 21) and player_turn == 1: 
         print("Final hand: " + str(value) + ".")
         player_1 = value
     elif value == 21: 
         print("Final hand: 21.")
         print("BLACKJACK!")
         if player_turn == 0:
             player_0 = value
         elif player_turn == 1:
             player_1 = value
     elif value > 21:
         print("Final hand: " + str(value) + ".")
         print("BUST.")
         if player_turn == 0:
             player_0 = value
         elif player_turn == 1:
             player_1 = value

     value = 0
     player_turn = player_turn + 1

print("-----------")
print("GAME RESULT")
print("-----------")

if (player_0 == player_1) or (player_1 > 21 and player_0 > 21):
     print("Tie.")
elif player_0 == 21:
     print("You win!")
elif player_1 == 21:
     print("Dealer wins!") 
elif player_0 < player_1 and not player_0 > 21 and player_1 > 21:
     print("You win!")
elif player_1 < player_0 and not player_1 > 21 and player_0 > 21:
     print("Dealer wins!")
elif player_1 in range(18, 21) and player_1 > player_0:
     print("Dealer wins!")
else:
     print("You win!")
    
     


