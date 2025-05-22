from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = list()
        if not root:
            return output

        def bfs(root):
            current_level = list()
            node = root
            current_level.append(node)
            while current_level:
                next_level = list()
                for node in current_level:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                output.append(current_level[-1].val)
                current_level = next_level
        
        bfs(root)
        return output

