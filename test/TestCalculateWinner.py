import unittest
from src.CalculateWinner import CalculateWinner

class TestCalculateWinner(unittest.TestCase):
      
    def setUp(self):
        self.calculator = CalculateWinner()

    def test_read_data(self):
        data = self.calculator.read_data('assets/votes.csv')
        for row in data:
            self.assertIsInstance(row, list)
            self.assertEqual(len(row), 6)

    def test_is_valid_dni(self):
        valid_dni = '12345678'
        invalid_dni = '12345'
        self.assertTrue(self.calculator.is_valid_dni(valid_dni))
        self.assertFalse(self.calculator.is_valid_dni(invalid_dni))

    def test_calculate_winner(self):
        test_data = [
            ['Region1', 'Province1', 'District1', '12345678', 'Candidate1', '1'],
            ['Region1', 'Province1', 'District1', '23456789', 'Candidate2', '1'],
            ['Region1', 'Province1', 'District1', '34567890', 'Candidate1', '1'],
            ['Region1', 'Province1', 'District1', '45678901', 'Candidate2', '0']
        ]
        winners = self.calculator.determine_winner(test_data)
        self.assertEqual(winners, ['Candidate1'])
