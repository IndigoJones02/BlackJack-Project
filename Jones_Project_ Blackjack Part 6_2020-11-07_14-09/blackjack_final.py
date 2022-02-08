# DO NOT REMOVE
from deck import print_card, draw_card, print_header, draw_starting_hand, print_end_turn_status, print_end_game_status

turn = 0 

while turn < 2:
     if turn == 0:
       user_hand = draw_starting_hand("YOUR")
     else:
       dealer_hand = draw_starting_hand('DEALER')
       
     if turn == 0 and user_hand != 21:
         answer = input('You have ' + str(user_hand) + '. Hit (y/n)? ')
             
     while (answer == 'y' and user_hand < 21) or (turn == 1 and dealer_hand < 17):
         if turn == 0:
             user_hand = user_hand + draw_card()
             if user_hand < 21:
                answer = input('You have ' + str(user_hand) + '. Hit (y/n)? ')
         else: 
             dealer_hand = dealer_hand + draw_card()
     
     if turn == 0:
        print_end_turn_status(user_hand)
     else:
         print_end_turn_status(dealer_hand)
     
     turn = turn + 1 
     
print_end_game_status(user_hand, dealer_hand)
     
     
