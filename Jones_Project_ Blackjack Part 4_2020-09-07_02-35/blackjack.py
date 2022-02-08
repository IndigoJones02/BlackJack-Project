from random import randint

turn = 0

while turn < 2
#unnecessary function (delete)
     if turn == 0:
         print('-----------')
#unnecessary function (delete)
         print('YOUR TURN')
#unnecessary function (delete)
         print('-----------')
     else:
         print('-----------')
         print('DEALER TURN')
         print('-----------')
#unnecessary funtion (delete)
#it exlains the function (delete)
     card1 = randint(1, 13) #bad variable naming 
     card1_value = 0
     
     if card1 == 1:
        card1_value = 11
        print("Drew a Ace") #Bad variable naming. Not printing anything.
 #delete lines 14 through 19 (will be included in else statement)
     elif card1 == 11:
        card1_value = 10
        print("Drew a Jack") #not printing anything out
 #delete lines 22 through 31 (will be included in else statement)
 #not printing anything
#delete lines 34 and 35 (will be included in else statement)
     elif card1 == 12:
        card1_value = 10
        print("Drew a Queen")
     elif card1 == 13:
        card1_value = 10
        print("Drew a King") #not printing anything
     else: #The else statement is being misused since the code is wriiten for all the numbers in the randint(1, 13).
        card1_value = card1
        print('Drew a ' + str(card1)) 
#no appropriate spacing (add spacing)
 #can combine lines 42 through47 and lines 48 and 49 and need better variables names for lines 42 through 51
#no appropriate spacing (add spacing)
#get randint #explains the function out (delete)
     card2 = randint(1, 13) #need a different variable name to differentiate between the two blocks of code
     card2_value = 0
     
     if card2 == 1:
        card2_value = 11
        print("Drew a Ace") #not printing out anything
#delete lines 57 through 62 (will be included in else statement)
     elif card2 == 11:
        card2_value = 10
        print("Drew a Jack") #not printing anything out 
#delete lines 65 through 74 (will be included in else statement)
     elif card2 == 12:
        card2_value = 10
        print("Drew a Queen") #not printing anything out
#delete lines 77 and 78 (will be included in else statement)
     elif card2 == 13:
        card2 = 10
        print("Drew a King") #not printing anything out
     else: #The else statement is being misused since the code is wriiten for all the numbers in the randint(1, 13).
 #unnecessary function (delete)
        card2_value = card2 
        print('Drew a ' + str(card2))
#no spacing (add spacing)
#no spacing (add spacing)
#add #unnecessary comment and its self-explainatory (delete)
     value = card1_value + card2_value #Better variable naming is needed and v2 is not defined. Also, int function is not needed (delete int()) and nothing is being printed out.
     if turn == 0 and value < 21:
        answer = input('You have ' + str(u) + '. Hit (y/n)? ')

     while (value < 21 and answer == 'y') or (turn == 1 and value >= 17): #unnecessary parenthesis and while statement could be simplified by setting input it equal to a variable and letting that variable be set equal to "y"
  #get randint #unnecessary comment (delete it)
         cards = randint(1, 13) #needs a different varaible name
         if cards == 1:
             cards_value = 11
             print("Drew a Ace")
 #delete lines 104 through 109 (will be included in else statement)
         elif cards == 11:
             cards_value = 10
             print("Drew a Jack")
 #delete lines 112 through 121 (will be included in else statement)
         elif cards == 12:
             cards_value = 10
             print("Drew a Queen")
 #delete lines 124 and 125(will be included in else statement)
         elif cards == 13:
             cards_value = 10
             print("Drew a King")
         else: 
 #delete line because does not change
             cards_value = cards
             print('Drew a ' + str(cards)) #change variable name to the new variable name of the card
#no spacing (add spacing)
#needs a different variable name for lines 132 through 141
#can combine lines 132 through 135 and lines 138 and 139
#add #delete comment (it self explauins the function)
         value = value + cards_value #needs better varable naming
#no spacing (add spacing)
         if turn == 0 and value < 21:
            answer = input('You have ' + str(value) + '. Hit (y/n)? ')
         else:
               print('Dealer has ' + str(value) + '.')

     dealer_hand = 0
     user_hand = 0
     
     if value == 21:
 #delete lines 146, 149, 151, and 152 and write it before the conditional statements
         print('BLACKJACK!')
         if turn = 0:
             user_hand = 21
         else:
             dealer_hand = 21
     elif value > 21:
         print('BUST.')
         if turn = 0:
             user_hand = value
         else:
             dealer_hand = value
     else:
         print('Final hand: ' + str(value) + '.')
         if turn = 0:
             user_hand = value
         else:
             dealer_hand = value
     turn = turn + 1
#delete lines 161 through 201 and place them in a while loop in the beghinning and can add lines 155, 157, and 159 in the begining and place it in a while loop.
 #delete function (there is no purpose of it)
 #delete function (there is no purpose of it)
 #delete function (there is no purpose of it)
# delete lines 202 through 244 and add it to the while loop in line 99
#delete comment 
#delete 248 through 255  because there wll be the same block of code after the first while loop

#delete unnecessary  function
print('-----------')
#delete unnecessary  function
print('GAME RESULT')
#delete unnecessary  function
print('-----------')
# no spacing (add spacing)
if dealer_hand <= 21 and user_hand > 21: : #delete extra colon
#add spacing between operands and delete unnecessary parenthesis and varaibles are undefined
  print('Dealer wins!')
elif user_hand <= 21 and dealer_hand > 21 #add colon
#add spacing between operands and delete unnecessary parenthesis
  print('You win!')
elif user_hand == dealer_hand or (user_hand > 21 and dealer_hand > 21) : #add spacing between operands and delete unnecessary parenthesis and simplify elif statement and lines 274 and 278  can be combined with this line
  print('Tie.')
elif dealer_hand <= 21 and user_hand <= 21 and dealer_hand > user_hand: #add spacing between operands and delete unnecessary parenthesis
  print('Dealer wins!')
#add spacing between operands and delete unnecessary parenthesis 
elif user_hand <= 21 and  dealer_hand <= 21 and user_hand > dealer_hand:
  print('You win!')
: #add spacing between operands and delete unnecessary parenthesis

