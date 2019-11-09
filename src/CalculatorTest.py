import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)
    def test_results_properties(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
