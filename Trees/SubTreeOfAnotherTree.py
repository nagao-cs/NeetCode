# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            elif (root and not subRoot) or (not root and subRoot):
                return False
            if root.val != subRoot.val:
                return False
            left = is_sameTree(root.left, subRoot.left)
            right = is_sameTree(root.right, subRoot.right)

            return left and right

        def dfs(root, subRoot):
            if not root:
                return False
            if root.val == subRoot.val:
                left = is_sameTree(root.left, subRoot.left)
                right = is_sameTree(root.right, subRoot.right)
                if left and right:
                    return True
                

            if dfs(root.left, subRoot):
                return True
            if dfs(root.right, subRoot):
                return True

            return False
        
        return dfs(root, subRoot)