from typing import Optional
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        str_tree = ''
        if not root:
            return str_tree
        def preorder(node):
            nonlocal str_tree
            if not node:
                str_tree += 'null,'
                return 
            str_tree += f"{node.val},"
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return str_tree

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(',')
        nodes.pop()
        if not nodes:
            return None
        i = 0
        def buildTree():
            nonlocal i
            val = nodes[i]
            i += 1
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = buildTree()
            node.right = buildTree()
            return node
        root = buildTree()
        return root
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))