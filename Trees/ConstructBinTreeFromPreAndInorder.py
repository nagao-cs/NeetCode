# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        head = TreeNode(preorder[0])
        i = 0
        while inorder[i] != preorder[0]:
            i += 1
        num_left = len(inorder[:i])
        num_right = len(inorder) - num_left - 1

        head.left = self.buildTree(preorder[1:1+num_left], inorder[:i])
        head.right = self.buildTree(preorder[num_left+1:], inorder[i+1:])

        return head