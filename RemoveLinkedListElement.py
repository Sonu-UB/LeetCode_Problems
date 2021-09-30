from typing import Optional

class ListNode:
    def __init__(self,value=0,next=None) -> None:
        self.value=value
        self.next = next

def removeElement(head:Optional[ListNode],val:int)->Optional[ListNode] :
    dummy_head = ListNode(-1)
    dummy_head.next = head

    current_node = dummy_head
    while current_node.next!=None:
        if current_node.next.value == val:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next

    return dummy_head.next


head = [1,2,6,4,5,6]
val = 6
print(removeElement(head,val))