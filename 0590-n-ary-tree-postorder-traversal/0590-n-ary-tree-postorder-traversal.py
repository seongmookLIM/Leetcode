"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        self.traverse(root, result)
        return result
    
    def traverse(self, root, result):
        if root:
            for child in root.children:
                self.traverse(child, result)
            result.append(root.val)