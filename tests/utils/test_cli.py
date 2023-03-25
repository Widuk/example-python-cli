from io import StringIO
import unittest
from unittest.mock import patch

from src.utils.cli import ask_yes_or_no

class TestCli(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_message_print(self, mock_stdout):
        with patch('builtins.input', return_value='yes'):
            respuesta = ask_yes_or_no('Continue? (yes/no): ')
        self.assertEqual(respuesta, True)
        self.assertEqual(mock_stdout.getvalue(), 'Continue? (yes/no): \n')
 
    def test_valid_response_yes(self):
        with patch('builtins.input', return_value='yes'):
            respuesta = ask_yes_or_no('Continue? (yes/no): ')
        self.assertEqual(respuesta, True)
 
    def test_valid_response_no(self):
        with patch('builtins.input', return_value='no'):
            respuesta = ask_yes_or_no('Continue? (yes/no): ')
        self.assertEqual(respuesta, False)
 
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_response(self, mock_stdout):
        with patch('builtins.input', side_effect=['something else', 'yes']):
            respuesta = ask_yes_or_no('a ')
        self.assertEqual(respuesta, True)
        self.assertEqual(mock_stdout.getvalue(), 'a \nPlease enter \'yes\' or \'no\'\na \n')