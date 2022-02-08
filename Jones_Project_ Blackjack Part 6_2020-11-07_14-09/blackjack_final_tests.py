from importlib import reload
from unittest import TestCase, main
from unittest.mock import patch
import io
import sys

def print_value(question, answer):
    print(question + answer)
    return answer

def run_test(user_cards, answers, dealer_cards, randint_mock, input_mock, imported):
    """
    Mocks randint and runs function with mock

    Args:
      randint_mock - patched random.randint()
      cards - desired input for random.randint()
      input_mock - patched bultins.input()
      answers - desired input for builtins.input()
      imported - whether module was imported already; always pass in True for your tests
    """
    answers.reverse() # reverses answers so can pop off list
    randint_mock.side_effect = user_cards + dealer_cards # set randint calls to cards
    input_mock.side_effect = \
        lambda question: print_value(question, answers.pop()) # print input question along with given answer

    # Save printed output into variable so can return it to compare in test
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    import blackjack_final
    if imported:
        reload(blackjack_final)
    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    return output # return printed statements in student-run code

class BlackjackPart6Test(TestCase):

    @patch('random.randint')
    @patch('builtins.input')
    def test_0_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''

        # Pass in True as the last argument in all your tests
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock, False)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.
    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    @patch('random.randint')
    @patch('builtins.input')
    def test_1_example(self, input_mock, randint_mock):
        '''
        The dealer recieves cards that result in a bust, while user recieve cards less than 21. 
        User ends up winning by not having cards over 21 and being closer than 21 without going over 21. 
        '''
        output = run_test([8, 7], ['n'], [6, 11, 6], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 8\n" \
                   "Drew a 7\n" \
                   "You have 15. Hit (y/n)? n\n" \
                   "Final hand: 15.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a Jack\n" \
                   "Drew a 6\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n" 
        self.assertEqual(output, expected)
        
    @patch('random.randint')
    @patch('builtins.input')
    def test_2_example(self, input_mock, randint_mock):
        '''
        The dealer recieves cards that are less than 21, while the user has cards over 21 resulting the dealer to winning.
        '''
        output = run_test([2, 10, 4, 10], ['y', 'y'], [6, 4, 9], randint_mock, input_mock, True)
        expected = '-----------\n' \
                   'YOUR TURN\n' \
                   '-----------\n' \
                   'Drew a 2\n' \
                   'Drew a 10\n' \
                   'You have 12. Hit (y/n)? y\n' \
                   'Drew a 4\n'\
                   'You have 16. Hit (y/n)? y\n' \
                   'Drew a 10\n' \
                   'Final hand: 26.\n' \
                   'BUST.\n' \
                   '-----------\n' \
                   'DEALER TURN\n' \
                   '-----------\n' \
                   'Drew a 6\n' \
                   'Drew a 4\n' \
                   'Drew a 9\n' \
                   'Final hand: 19.\n' \
                   '-----------\n' \
                   'GAME RESULT\n' \
                   '-----------\n' \
                   'Dealer wins!\n'
        self.assertEqual(output, expected)
        
    @patch('random.randint')
    @patch('builtins.input')
    def test_3_example(self, input_mock, randint_mock):
        '''
        The dealer recieves cards that equals 21 and user recieves cards that equal 21, resulting in a tie.
        '''
        output = run_test([10, 1], [], [6, 4, 1], randint_mock, input_mock, True)
        expected = '-----------\n' \
                   'YOUR TURN\n' \
                   '-----------\n' \
                   'Drew a 10\n' \
                   'Drew a Ace\n' \
                   'Final hand: 21.\n' \
                   'BLACKJACK!\n' \
                   '-----------\n' \
                   'DEALER TURN\n' \
                   '-----------\n' \
                   'Drew a 6\n' \
                   'Drew a 4\n' \
                   'Drew a Ace\n' \
                   'Final hand: 21.\n' \
                   'BLACKJACK!\n' \
                   '-----------\n' \
                   'GAME RESULT\n' \
                   '-----------\n' \
                   'Tie.\n'
        self.assertEqual(output, expected)
     
    @patch('random.randint')
    @patch('builtins.input')    
    def test_4_example(self, input_mock, randint_mock):
        '''
        The dealer recieves cards that are over 21, and the user has cards over 21 resulting in a tie.
        '''
        output = run_test([2, 10, 4, 10], ['y', 'y'], [10, 4, 9], randint_mock, input_mock, True)
        expected = '-----------\n' \
                   'YOUR TURN\n' \
                   '-----------\n' \
                   'Drew a 2\n' \
                   'Drew a 10\n' \
                   'You have 12. Hit (y/n)? y\n' \
                   'Drew a 4\n' \
                   'You have 16. Hit (y/n)? y\n' \
                   'Drew a 10\n' \
                   'Final hand: 26.\n' \
                   'BUST.\n' \
                   '-----------\n' \
                   'DEALER TURN\n' \
                   '-----------\n' \
                   'Drew a 10\n' \
                   'Drew a 4\n' \
                   'Drew a 9\n' \
                   'Final hand: 23.\n' \
                   'BUST.\n' \
                   '-----------\n' \
                   'GAME RESULT\n' \
                   '-----------\n' \
                   'Tie.\n'
        self.assertEqual(output, expected)
    
    @patch('random.randint')
    @patch('builtins.input')
    def test_5_example(self, input_mock, randint_mock):
        '''
        The dealer and user recieves cards that are less than 21 and are equal to each other resulting into a tie
        '''
        output = run_test([5, 5, 2, 7], ['y', 'y', 'n'], [6, 4, 9], randint_mock, input_mock, True)
        expected = '-----------\n' \
                   'YOUR TURN\n' \
                   '-----------\n' \
                   'Drew a 5\n' \
                   'Drew a 5\n' \
                   'You have 10. Hit (y/n)? y\n' \
                   'Drew a 2\n' \
                   'You have 12. Hit (y/n)? y\n' \
                   'Drew a 7\n' \
                   'You have 19. Hit (y/n)? n\n' \
                   'Final hand: 19.\n' \
                   '-----------\n' \
                   'DEALER TURN\n' \
                   '-----------\n' \
                   'Drew a 6\n' \
                   'Drew a 4\n' \
                   'Drew a 9\n' \
                   'Final hand: 19.\n' \
                   '-----------\n' \
                   'GAME RESULT\n' \
                   '-----------\n' \
                   'Tie.\n'
        self.assertEqual(output, expected)
        
    @patch('random.randint')
    @patch('builtins.input')
    def test_6_example(self, input_mock, randint_mock):
        '''
        The dealer and user recieves cards that are less than 21, but user cards is less than the dealers cards resulting in the dealers win.
        '''
        output = run_test([6, 7], ['n'], [6, 4, 9], randint_mock, input_mock, True)
        expected = '-----------\n' \
                   'YOUR TURN\n' \
                   '-----------\n' \
                   'Drew a 6\n' \
                   'Drew a 7\n' \
                   'You have 13. Hit (y/n)? n\n' \
                   'Final hand: 13.\n' \
                   '-----------\n' \
                   'DEALER TURN\n' \
                   '-----------\n' \
                   'Drew a 6\n' \
                   'Drew a 4\n' \
                   'Drew a 9\n' \
                   'Final hand: 19.\n' \
                   '-----------\n' \
                   'GAME RESULT\n' \
                   '-----------\n' \
                   'Dealer wins!\n'
        self.assertEqual(output, expected)
        
    @patch('random.randint')
    @patch('builtins.input')
    def test_7_example(self, input_mock, randint_mock):
        '''
        The dealer and user recieves cards that are less than 21 but user's hand is greater than the dealer's hand resulting in the user's win.
        '''
        output = run_test([5, 5, 13], ['y', 'n'], [3, 7, 8], randint_mock, input_mock, True)
        expected = '-----------\n' \
                   'YOUR TURN\n' \
                   '-----------\n' \
                   'Drew a 5\n' \
                   'Drew a 5\n' \
                   'You have 10. Hit (y/n)? y\n' \
                   'Drew a King\n' \
                   'You have 20. Hit (y/n)? n\n' \
                   'Final hand: 20.\n' \
                   '-----------\n' \
                   'DEALER TURN\n' \
                   '-----------\n' \
                   'Drew a 3\n' \
                   'Drew a 7\n' \
                   'Drew a 8\n' \
                   'Final hand: 18.\n' \
                   '-----------\n' \
                   'GAME RESULT\n' \
                   '-----------\n' \
                   'You win!\n'
        self.assertEqual(output, expected)
        
    @patch('random.randint')
    @patch('builtins.input')
    def test_8_example(self, input_mock, randint_mock):
        '''
        The dealer card equal to 21 and user card are over 21 resulting in the dealers win.
        '''
        output = run_test([3, 8, 9, 3], ['y', 'y'], [11, 1], randint_mock, input_mock, True)
        expected = '-----------\n' \
                   'YOUR TURN\n' \
                   '-----------\n' \
                   'Drew a 3\n' \
                   'Drew a 8\n' \
                   'You have 11. Hit (y/n)? y\n' \
                   'Drew a 9\n' \
                   'You have 20. Hit (y/n)? y\n' \
                   'Drew a 3\n' \
                   'Final hand: 23.\n' \
                   'BUST.\n' \
                   '-----------\n' \
                   'DEALER TURN\n' \
                   '-----------\n' \
                   'Drew a Jack\n' \
                   'Drew a Ace\n' \
                   'Final hand: 21.\n' \
                   'BLACKJACK!\n' \
                   '-----------\n' \
                   'GAME RESULT\n' \
                   '-----------\n' \
                   'Dealer wins!\n'
        self.assertEqual(output, expected)
        
    @patch('random.randint')
    @patch('builtins.input')
    def test_9_example(self, input_mock, randint_mock):
        '''
        The dealer receives cards less than 21 and the user receives cards that equal 21 resulting in the user win.
        '''
        output = run_test([2, 8, 7, 4], ['y', 'y'], [6, 4, 9], randint_mock, input_mock, True)
        expected = '-----------\n' \
                   'YOUR TURN\n' \
                   '-----------\n' \
                   'Drew a 2\n' \
                   'Drew a 8\n' \
                   'You have 10. Hit (y/n)? y\n' \
                   'Drew a 7\n' \
                   'You have 17. Hit (y/n)? y\n' \
                   'Drew a 4\n' \
                   'Final hand: 21.\n' \
                   'BLACKJACK!\n' \
                   '-----------\n' \
                   'DEALER TURN\n' \
                   '-----------\n' \
                   'Drew a 6\n' \
                   'Drew a 4\n' \
                   'Drew a 9\n' \
                   'Final hand: 19.\n' \
                   '-----------\n' \
                   'GAME RESULT\n' \
                   '-----------\n' \
                   'You win!\n'
        self.assertEqual(output, expected)
        

    @patch('random.randint')
    @patch('builtins.input')
    def test_9_example(self, input_mock, randint_mock):
        '''
        The user receives cards equal to 21 and the dealer recieves cards that are over 21. Resulting in the users win.
        '''
        output = run_test([2, 8, 7, 4], ['y', 'y'], [11, 4, 9], randint_mock, input_mock, True)
        expected = '-----------\n' \
                   'YOUR TURN\n' \
                   '-----------\n' \
                   'Drew a 2\n' \
                   'Drew a 8\n' \
                   'You have 10. Hit (y/n)? y\n' \
                   'Drew a 7\n' \
                   'You have 17. Hit (y/n)? y\n' \
                   'Drew a 4\n' \
                   'Final hand: 21.\n' \
                   'BLACKJACK!\n' \
                   '-----------\n' \
                   'DEALER TURN\n' \
                   '-----------\n' \
                   'Drew a Jack\n' \
                   'Drew a 4\n' \
                   'Drew a 9\n' \
                   'Final hand: 23.\n' \
                   'BUST.\n' \
                   '-----------\n' \
                   'GAME RESULT\n' \
                   '-----------\n' \
                   'You win!\n'
        self.assertEqual(output, expected)
    
    @patch('random.randint')
    @patch('builtins.input')
    def test_9_example(self, input_mock, randint_mock):
        '''
        The dealer receives cards that equal to 21 and the user receives cards less than 21 resulting the dealer to win.
        '''
        output = run_test([2, 8, 7], ['y', 'n'], [1, 10], randint_mock, input_mock, True)
        expected = '-----------\n' \
                   'YOUR TURN\n' \
                   '-----------\n' \
                   'Drew a 2\n' \
                   'Drew a 8\n' \
                   'You have 10. Hit (y/n)? y\n' \
                   'Drew a 7\n' \
                   'You have 17. Hit (y/n)? n\n' \
                   'Final hand: 17.\n' \
                   '-----------\n' \
                   'DEALER TURN\n' \
                   '-----------\n' \
                   'Drew a Ace\n' \
                   'Drew a 10\n' \
                   'Final hand: 21.\n' \
                   'BLACKJACK!\n' \
                   '-----------\n' \
                   'GAME RESULT\n' \
                   '-----------\n' \
                   'Dealer wins!\n'
        self.assertEqual(output, expected)
    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()
