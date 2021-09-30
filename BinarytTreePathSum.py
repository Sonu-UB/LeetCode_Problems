class TreeNode:
    def __init__(self,val,right,left):
        self.val = val
        self.left = None
        self.right = None

def hasPathSum(root,targetSum):
    if not root:
        return False
    
    if not root.left and not root.right and root.val == targetSum:
        return True

    targetSum -= root.val

    return hasPathSum(root.left,targetSum) or hasPathSum(root.right,targetSum)