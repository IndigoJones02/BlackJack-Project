from deck import print_card, draw_card, print_header, draw_starting_hand, print_end_turn_status, print_end_game_status
from deck_test_helper import get_print, mock_random
import unittest
from unittest.mock import patch


class TestBlackjack(unittest.TestCase):
  """
  Class for testing Blackjack.

  There are two helper functions, get_print and mock_random, that can help you.

  get_print: returns the printed statements from running a provided function with provided arguments
  mock_random: use this if code calls randint. mock_random takes in a list of numbers that randint should
               be using and runs the provided function with provided arguments accordingly

  Example of calling print_card, which takes an argument and prints out card rank:
    get_print(print_card, 2) - returns string that gets printed out when print_card function gets called with 2
    To check whether the above printed correctly - self.assertEqual(get_print(print_card, 2), "Drew a 2\n")
    
  Example of calling draw_card(), which takes no arguments but uses randint:
    mock_random([3], draw_card)) - runs draw_card with 3 as the randint
    To check whether the above returned correctly - self.assertEqual(mock_random([3], draw_card)), 3)

    If the function takes in an argument, pass that as the last argument into mock_random()
    mock_random([3, 5], draw_starting_hand), "DEALER") - runs draw_starting_hand with 3 as first randint, 5 as second
    To check whether the above returned correctly - self.assertEqual(mock_random([3, 5], draw_starting_hand), "DEALER")
  """

  def test_print_card(self):
    """
    Example of a test to compare printed statements with expected

    This does not count as one of your tests
    """
    self.assertEqual(get_print(print_card, 2), "Drew a 2\n")

  def test_mock_randint(self):
    """
    Example of a test to compare output for a function that calls randint

    This does not count as one of your tests
    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

  # WRITE YOUR TESTS BELOW
  def test_print_card(self):
    self.assertEqual(get_print(print_card, 11), "Drew a Jack\n")
    self.assertEqual(get_print(print_card, 12), 'Drew a Queen\n')
    self.assertEqual(get_print(print_card, 13), 'Drew a King\n')
    self.assertEqual(get_print(print_card, 1), 'Drew a Ace\n')
    self.assertEqual(get_print(print_card, 3), 'Drew a 3\n')
    self.assertEqual(get_print(print_card, 8), 'Drew a 8\n') 

  def test_draw_card(self):   
    self.assertEqual(mock_random([1], draw_card), 11)
    self.assertEqual(mock_random([11], draw_card), 10)
    self.assertEqual(mock_random([12], draw_card), 10)
    self.assertEqual(mock_random([13], draw_card), 10)
    self.assertEqual(mock_random([7], draw_card), 7)
    self.assertEqual(mock_random([4], draw_card), 4)

  def test_print_header(self):
    self.assertEqual(get_print(print_header, "YOUR TURN"), '-----------\nYOUR TURN\n-----------\n')
    self.assertEqual(get_print(print_header, "DEALER TURN"), '-----------\nDEALER TURN\n-----------\n')
    self.assertEqual(get_print(print_header, "GAME RESULT"), '-----------\nGAME RESULT\n-----------\n')
    self.assertEqual(get_print(print_header, " "), '-----------\n \n-----------\n')

  def test_draw_starting_hand(self):
    self.assertEqual(mock_random([1, 11], draw_starting_hand, "DEALER"), 21)
    self.assertEqual(mock_random([2, 13], draw_starting_hand, 'DEALER'), 12)
    self.assertEqual(mock_random([11, 12], draw_starting_hand, 'USER'), 20)
    self.assertEqual(mock_random([13, 1], draw_starting_hand, 'USER'), 21) 
    self.assertEqual(mock_random([2, 3], draw_starting_hand, 'USER'), 5)
    self.assertEqual(mock_random([5, 1], draw_starting_hand, 'DEALER'), 16)

  def test_print_end_turn_status(self):
    self.assertEqual(get_print(print_end_turn_status, 21), "Final hand: 21.\nBLACKJACK!\n")
    self.assertEqual(get_print(print_end_turn_status, 25), "Final hand: 25.\nBUST.\n")
    self.assertEqual(get_print(print_end_turn_status, 33), "Final hand: 33.\nBUST.\n")
    self.assertEqual(get_print(print_end_turn_status, 17), "Final hand: 17.\n")
    self.assertEqual(get_print(print_end_turn_status, 19), "Final hand: 19.\n")
    self.assertEqual(get_print(print_end_turn_status, 5), "Final hand: 5.\n")

  def print_end_game_status(self):
    self.assertEqual(get_print(print_end_game_status, 21, 21), "-----------\nGAME RESULT\n-----------\nTie.\n")
    self.assertEqual(get_print(print_end_game_status, 21, 10), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 18, 21), "-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 21, 25), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 26, 21), "-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 19, 19), "-----------\nGAME RESULT\n-----------\nTie.\n")
    self.assertEqual(get_print(print_end_game_status, 28, 28), "-----------\nGAME RESULT\n-----------\nTie.\n")
    self.assertEqual(get_print(print_end_game_status, 5, 24), "-----------\nGAME RESULT\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 18, 7), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 22, 24), "-----------\nGAME RESULT\nTie.\n")

  # Make sure all test function names start with test_




if __name__ == '__main__':
    unittest.main()
