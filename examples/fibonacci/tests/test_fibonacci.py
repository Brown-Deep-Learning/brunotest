import unittest
from gradescope_utils.autograder_utils.decorators import number, weight


class TestFibonacci(unittest.TestCase):

    @number('1')
    @weight(25)
    def test_base_cases(self):
        """
        Base case values are correct
        """
        pass

    @number('2')
    @weight(75)
    def test_general(self):
        """
        General computation cases for fibonacci are correct
        """
        pass
