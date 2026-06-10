# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0

        stack = deque()

        depth = 1
        stack.appendleft(root)

        while stack:
            
            n = len(stack)
            for i in range(n) :
                node = stack.pop()
                
                if node.left:
                    stack.appendleft(node.left)
                
                if node.right:
                    stack.appendleft(node.right)
 
            if stack:
                depth +=1
            
        return depth
        