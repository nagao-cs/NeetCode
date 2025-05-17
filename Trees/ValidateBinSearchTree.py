# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def is_valid_recursive(node, min_val=-2**31-1, max_val=2**31) -> bool:
            if not node:
                return True
            # print(node.val, min_val, max_val)
            
            if not (min_val < node.val < max_val):
                return False
            return is_valid_recursive(node.left, min_val, node.val) and is_valid_recursive(node.right, node.val, max_val)

        return is_valid_recursive(root)