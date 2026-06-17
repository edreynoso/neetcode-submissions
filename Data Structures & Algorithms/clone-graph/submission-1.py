"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return 
        
        seen = set()
        
        clone_map = {}

        stack = deque()

        stack.append(node)

        while stack:
            head = stack.pop()
            seen.add(head.val)
            clone_map[head.val] = [n.val for n in head.neighbors] 
            for n in head.neighbors:
                if n.val not in seen:
                    stack.append(n)
                    seen.add(n.val)

        nodes = {val: Node(val) for val in clone_map}

        for val, neighbors in clone_map.items():
            nodes[val].neighbors = [nodes[n] for n in neighbors]

        return nodes[node.val]
        
        