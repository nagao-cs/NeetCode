from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        dp = list() #dp[i]はnode_iを通った場合の最大のパス
        maxPath = -1001
        i = -1
        def postorder(node):
            nonlocal i
            nonlocal maxPath
            val = node.val
            if node.left:
                postorder(node.left)
                left = i
            if node.right:
                postorder(node.right)
                right = i
            i += 1
            if node.left and node.right:
                dp.append(max(dp[left]+val, dp[right]+val, val))
                maxPath = max(maxPath, dp[left]+dp[right]+val, dp[-1])
            elif node.left:
                dp.append(max(dp[left]+val, val))
                maxPath = max(maxPath, dp[-1])
            elif node.right:
                dp.append(max(dp[right]+val, val))
                maxPath = max(maxPath, dp[-1])
            else:
                dp.append(val)
                maxPath = max(maxPath, dp[-1])

        postorder(root)
        return maxPath