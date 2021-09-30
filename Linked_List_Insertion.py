# THIS IS THE CODE TO INSERT ELEMENTS IN THE LINKED LINST AT DIFFERENT POSITIONS

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to insert a new node at given position
    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print("The given node must intLinkedlist")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Funtion to append a new node at the end
    def append(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while(last.next):
            last = last.next
        
        last.next = new_node

    #----------TO PRINT THE LINKED LIST------------------
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    # ----------------------------------------------------

# Code Execution 
if __name__ == '__main__':
    llist = LinkedList()
    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.append(4)

    llist.insertAfter(llist.head.next,8)

    print("Created linked list is:")
    llist.printList()

