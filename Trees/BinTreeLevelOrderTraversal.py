# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output = list()

        nodes = list() #現在の深さのノード
        nodes.append(root)
        while len(nodes) > 0:
            output.append(list(node.val for node in nodes))
            next_nodes = list() #次の深さのノード
            for node in nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            nodes = next_nodes
                        
        return output