# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #左部分木の高さ+右部分木の高さ+2=rootの直径
        #木の高さ = max(左部分木の高さ、右部分木の高さ)

        def depth_of_tree(root: Optional[TreeNode]) -> int:
            depth_left = 0
            depth_right = 0
            if not (root.left or root.right):
                return 0
            if root.left:
                depth_left = depth_of_tree(root.left) + 1
            if root.right:
                depth_right = depth_of_tree(root.right) + 1
            return max(depth_left, depth_right)
        
        if not (root.left or root.right):
            return 0
        left_diameter, right_diameter = 0, 0
        left_depth, right_depth = 0, 0
        if root.left:
            left_diameter = self.diameterOfBinaryTree(root.left)
            left_depth = depth_of_tree(root.left) + 1
        if root.right:
            right_diameter = self.diameterOfBinaryTree(root.right)
            right_depth = depth_of_tree(root.right) + 1

        return max(left_diameter, right_diameter, left_depth+right_depth)