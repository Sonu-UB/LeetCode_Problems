class ListNode:
    def __init__(self,val,next):
        self.val = val
        self.next = next

def mergeTwolists(self,l1,l2):
    if not l1 and not l2:
        return l1

    merged_list = ListNode(-1)
    dummy_merge_list = merged_list

    while l1 or l2:
        if l1 and not l2:
            dummy_merge_list.val = l1.val
            l1 = l1.next
        elif not l1 and l2:
            dummy_merge_list.val = l2.val
            l2 = l2.next
        else:
            if l1.val < l2.val:
                dummy_merge_list.val = l1.val
                l1 = l1.next
            else:
                dummy_merge_list = l2.val
                l2 = l2.val
        
        if l1 or l2:
            dummy_merge_list.next = ListNode(None)
            dummy_merge_list = dummy_merge_list.next
    
    return merged_list
