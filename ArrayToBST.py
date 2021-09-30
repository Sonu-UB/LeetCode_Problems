from typing import List, Optional

class TreeNode:
    def __init__(self,val,left,right):
        self.val = val
        self.right = right
        self.left = left


def arrayToBST(nums:List[int])->Optional[TreeNode]:
    def helper(l,r):
        if l>r:
            return None
        
        m = (l+r)//2
        root = TreeNode(nums[m])
        root.left = helper(l,m-1)
        root.right = helper(m+1,r)
        return root

    return helper(0,len(nums-1))

    