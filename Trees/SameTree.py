# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        left = False
        right = False
        if not (p and q): #pとqがそもそもNoneならTrue
            if (p or q):
                return False 
            else:
                return True
        if p.left and q.left:
            left = self.isSameTree(p.left, q.left)
        else:
            left = not(p.left or q.left)
        if p.right and q.right:
            right =  self.isSameTree(p.right, q.right)
        else:
            right =  not(p.right or q.right)
        if left and right and p.val == q.val:
            return True
        else:
            return False
        
            