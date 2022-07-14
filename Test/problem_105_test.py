## testcase file for Lettcode problem 105
## author MDomalewski, generated by TypicalUsername-ai's leetcode python repository
## created on: 2022-07-14 10:25:52.777759

## import Structures ##uncomment if the task requires a non-basic data structure
import unittest
from Solutions import problem_105

class Problem_105_test(unittest.TestCase):
    def setUp(self):
        self.solution = problem_105.Solution()

    def test_empty(self):
        self.assertEqual(self.solution.buildTree([],[]), None)

st = unittest.defaultTestLoader.loadTestsFromTestCase(Problem_105_test)
unittest.TextTestRunner().run(st)