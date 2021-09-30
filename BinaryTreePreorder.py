from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, r = [], []
        while stack or root:
            if root:
                stack.append(root)
                r.append(root.val)
                root = root.left
            else:
                root = stack.pop().right
        return r