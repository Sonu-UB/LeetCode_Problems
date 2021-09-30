class TreeNode:
    def __init__(self,val,left,right):
        self.val = val
        self.left = None
        self.right = None

    
def searchBST(root, val):
    def recursive(root):
        if root:
            if root.val == val:
                return root
            elif root.val<val:
                return recursive(root.right)
            return recursive(root.left)

    return recursive(root)

