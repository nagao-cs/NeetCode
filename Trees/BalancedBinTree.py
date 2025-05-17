# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]) -> int:
            if root == None:
                return 0
            left = dfs(root.left) + 1
            right = dfs(root.right) + 1
            return max(left, right)

        if root == None:
            return True
        left = dfs(root.left)
        right = dfs(root.right)
        if abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False