## testcase file for Lettcode problem 102
## author MDomalewski, generated by TypicalUsername-ai's leetcode python repository
## created on: 2022-07-13 20:16:28.002464

from Structures import TreeNode as tr ##uncomment if the task requires a non-basic data structure
import unittest
from Solutions import problem_102

class Problem_102_test(unittest.TestCase):
    def setUp(self):
        self.solution = problem_102.Solution()

    def test_empty(self):
        l = tr.TreeNode(9)
        r = tr.TreeNode(20)
        t = tr.TreeNode(3, l, r)
        self.assertEqual(self.solution.levelOrder(t), [[3], [9,20]])

st = unittest.defaultTestLoader.loadTestsFromTestCase(Problem_102_test)
unittest.TextTestRunner().run(st)
