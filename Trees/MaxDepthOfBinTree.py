# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> int:
            if root == None:
                return 0
            left = dfs(root.left) + 1
            right = dfs(root.right) + 1

            return max(left, right)
        
        return dfs(root)