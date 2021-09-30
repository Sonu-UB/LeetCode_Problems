class TreeNode:
    def __init__(self,val,left,right):
        self.val = val
        self.left = None
        self.right = None

def invertTree(root):
    if root:
        root.left,root.right = invertTree(root.right),invertTree(root.left)

    return root