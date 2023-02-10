import unittest
from python_cases.case1 import fizzbuzz

class TestMain(unittest.TestCase):
    """
    Test harness
    """

    def test_fizzbuzz(self):
        """
        Test fizzbuzz
        """
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(0), str(0))
        self.assertEqual(fizzbuzz(-1), str(-1))

if __name__ == '__main__':
    unittest.main()