import unittest
from gradescope_utils.autograder_utils.decorators import number, weight

from brunotest import import_solution, import_student


class TestFibonacci(unittest.TestCase):
    @number("1")
    @weight(25)
    def test_base_cases(self):
        """
        Base case values are correct
        """
        student_fibonacci = import_student("fibonacci", "fibonacci")
        self.assertEqual(student_fibonacci.fibonacci(0), 0)
        self.assertEqual(student_fibonacci.fibonacci(1), 1)
        print("Base cases are correct!")

    @number("2")
    @weight(75)
    def test_general(self):
        """
        General computation cases for fibonacci are correct
        """
        student_fibonacci = import_student("fibonacci", "fibonacci")
        solution_fibonacci = import_solution("fibonacci", "fibonacci")

        for i in range(2, 1000):
            self.assertEqual(
                student_fibonacci.fibonacci(i), solution_fibonacci.fibonacci(i)
            )

        print("General cases are correct!")
