## solution class for Lettcode problem 199
## author MDomalewski, generated by TypicalUsername-ai's leetcode python repository
## created on: 2022-07-11 17:00:55.920599
from Structures import TreeNode #uncomment if the task requires a non-basic data structure
class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def solve(node, lvl):
            if node: #checks if node exists (node here is the function input)
                if len(res)==lvl: #appends if we're at correct height
                    res.append(node.val)
                solve(node.right, lvl + 1) #due to traversal order we always visit right first
                solve(node.left, lvl + 1) # so left only appends when the right is not in place -> this will work no matter the tree structure
            return 
        solve(root,0)
        return res
        
        
