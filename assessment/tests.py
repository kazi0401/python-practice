import unittest
from problems import *


class FizzBuzzTest(unittest.TestCase):
    '''
        Each function is a test!
        Each function must start with 'test_'

        use self.assertEqual() to check your result against
        your expected value

        Consider using:
            self.assertTrue()
            self.assertFalse()
            
    '''

    def test_100(self):
        res = fizzbuzz(100)
        expected = [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24,
                    25, 27, 30, 33, 35, 36, 39, 40, 42, 45,
                    48, 50, 51, 54, 55, 57, 60, 63, 65, 66,
                    69, 70, 72, 75, 78, 80, 81, 84, 85, 87,
                    90, 93, 95, 96, 99, 100]
        self.assertEqual(res, expected)

    def test_zero(self):
        res = fizzbuzz(0)
        expected = []
        self.assertEqual(res, expected)

class ReverseTest(unittest.TestCase):

    def test_basic(self):
        l = [1, 2, 3]
        res = reversal(l)
        expected = [3, 2, 1]

        self.assertEqual(res, expected)



class PalindromeTest(unittest.TestCase):

    def test_racecar(self):
        string = 'racecar'
        assert is_palindrome(string) == True



if __name__ == '__main__':
    unittest.main(defaultTest = 'PalindromeTest')
