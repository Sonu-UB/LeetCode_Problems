from queue import Queue

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def getLeafCount(node):

    if(not node):
        return 0
    
    q = Queue()

    count = 0
    q.put(node)
    while(not q.empty()):
        temp = q.queue[0]
        q.get()

        if(temp.left !=None):
            q.put(temp.left)
        if(temp.right != None):
            q.put(temp.right)
        if(temp.left == None and temp.right == None):
            count +=1
    return count

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    root.left.left = Node(4)

    print(getLeafCount(root))
