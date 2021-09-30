
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
def levelOrder( root: Optional[TreeNode]) -> List[List[int]]:
    h = height(root)
    for i in range(1,h-1):
        printCurrentLevel(root,i)
def printCurrentLevel(root,level):
    if root is None:
        return
    if level==1:
        print(root.val,end=" ")
    elif level>1:
        printCurrentLevel(root.left,level-1)
        printCurrentLevel(root.right,level-1)
def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1    
# -----------------------------------------------------------------
    # Iterative Way of doing this 
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    from collections import deque
    deque, ret = deque(), []
    if root:
        deque.append(root)
    while deque:
        level, size = [], len(deque)
        for _ in range(size):
            node = deque.popleft()
            level.append(node.val)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        ret.append(level)
    return ret
# -------------------------------------------------------------------



# Driver program to test above function
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
 
print("Level order traversal of binary tree is -")
levelOrder(root)