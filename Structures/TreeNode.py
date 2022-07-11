# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def initFromList(self, values: list[int], index: int = 1): #MAYBE add that fucntionality later
    #     self.val = values[index-1]
    #     if len(list) >= index*2:
    #         self.left = self.initFromList(values, index*2)
    #     if len(list) >= index*2 + 1:
    #         self.right = self.initFromList(values, index*2 +1)
    #     return self