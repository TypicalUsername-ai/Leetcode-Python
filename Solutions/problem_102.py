## solution class for Lettcode problem 102
## author MDomalewski, generated by TypicalUsername-ai's leetcode python repository
## created on: 2022-07-13 20:16:27.999463
from Structures import TreeNode as tr #uncomment if the task requires a non-basic data structure
class Solution(object):
    ## TODO solution code goes here
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        l_arr = []
        def traverse(level: int, node: tr.TreeNode):
            if level == len(l_arr):
                l_arr.append([])
            l_arr[level].append(node.val)
            if node.left:
                traverse(level+1, node.left)
            if node.right:
                traverse(level+1, node.right)

        traverse(0, root)
        return l_arr
