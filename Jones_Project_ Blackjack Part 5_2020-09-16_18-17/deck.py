import random

"""
#1

Function: print_card

Prints the given card's official name.

Args:
  card_rank: The numeric representation of a card.

Example:
  print_card(2) prints out
  Drew a 2

  print_card(11) prints out
  Drew a Jack 

"""
# Write code for #1 here

def print_card(card_rank):
     if card_rank == 11:
         card = "Jack"
     elif card_rank == 12:
         card = "Queen"
     elif card_rank == 13:
         card = "King"
     elif card_rank == 1:
         card = "Ace"
     else:
         card = str(card_rank)
     print("Drew a " + card)
"""
#2

Function: draw_card

Draws a new random card, prints its name, and returns its face value.

Returns:
  Face value of chosen card. Face value of a card is the same as numeric value,
  except for Ace, Jack, Queen, and King.

Examples:
  draw_card() returns 11 (if card drawn is Ace)
  draw_card() returns 4  (if card drawn is 4)
  draw_card() returns 10 (if card drawn is Jack, Queen, King)
"""
# Write code for #2 here

def draw_card():
     rank = random.randint(1, 13)
     if rank == 1: 
         print('Ace')
         card_value = 11
     elif rank >= 11 and rank <= 13:
         card_value = 10
         if rank == 11:
             print('Jack')
         elif rank == 12:
             print('Queen')
         elif rank == 13:
             print('King')
     else:
         print(str(rank))
         card_value = rank
     return card_value

"""
#3

Function: print_header

Prints the given message formatted as a header.

Args:
  message: The message to be printed.

Example:
  print_header("YOUR TURN") prints out
  -----------
  YOUR TURN
  ----------- 
"""
# Write code for #3 here

def print_header(message):
     message = str(message)
     if message == "YOUR TURN":
         print('-----------')
         print(message)
         print('-----------')
     else:
         print('-----------')
         print(message)
         print('-----------')
     
"""
#4

Function: draw_starting_hand

Prints turn header and draws a starting hand, which is two cards.

Args:
  name: The name of the player whose turn it is.

Returns:
  The hand total, which is the sum of the two newly drawn cards.
"""
# Write code for #4 here


def draw_starting_hand(name):
     name = str(name)
     if name == 'DEALER':
         print_header('DEALER TURN')
         turn = 0
         while turn < 2:
            if turn == 0:
                 card_drawn = draw_card()
            else:
                 another_card_drawn = draw_card()
            turn = turn + 1
     else:
         print_header('YOUR TURN')
         turn = 0
         while turn < 2:
            if turn == 0:
                 card_drawn = draw_card()
            else:
                 another_card_drawn = draw_card()
            turn = turn + 1
     hand_total = card_drawn + another_card_drawn
     return hand_total
"""
#5

Function: print_end_turn_status

Prints the hand total and status at the end of a player's turn.

Args:
  hand: The sum of of all the cards in the hand.

Examples:
  print_end_turn_status(15) prints out
  Final hand: 15.

  print_end_turn_status(21) prints out
  Final hand: 21.
  BLACKJACK!

  print_end_turn_status(25) prints out
  Final hand: 25.
  BUST.
"""
# Write code for #5 here

def print_end_turn_status(hand):
     if hand > 21:
         print("Final hand: " + str(hand) + '.')
         print("BUST.")
     elif hand < 21:
         print("Final hand: " + str(hand) + '.')
     else:
         print("Final hand: " + str(hand) + '.')
         print("BLACKJACK!") 
"""
#6

Function: print_end_game_status

Prints the end game banner and the winner based on the final hands.

Args:
  user_hand: The sum of all the cards in the user's hand.
  dealer_hand: The sum of all the cards in the dealer's hand.

Examples:
  print_end_game_status(18, 21) prints out
  -----------
  GAME RESULT
  -----------
  You win!

  print_end_game_status(21, 18) prints out
  -----------
  GAME RESULT
  -----------
  Dealer wins!

  print_end_game_status(24, 22) prints out
  -----------
  GAME RESULT
  -----------
  Tie.
"""
# Write code for #6 here

def print_end_game_status(dealer_hand, user_hand): 
     print_header('GAME RESULT')
     if user_hand == 21 and dealer_hand != 21:
         print('You win!')
     elif dealer_hand == 21 and user_hand != 21:
         print('Dealer wins!')
     elif dealer_hand in range(18, 21) and user_hand < 18 or user_hand > 21:
         print('Dealer wins!')
     elif user_hand > dealer_hand and dealer_hand != 21:
         print('You win!')
     elif user_hand < 21 and dealer_hand > 21:
         print('You win!')
     else: 
         print('Tie.')