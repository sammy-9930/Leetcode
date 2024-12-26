class Node:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 

class LinkedList:  
    def __init__(self):
        self.head = None 
         
    def traverse(self):
        current = self.head 
        while current is not None:
            print(current.val)
            current = current.next 
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node 
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return 
        current = self.head 
        while current.next:
            current = current.next 
        current.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head 
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            current = current.next 
        new_node.next = current.next
        current.next = new_node 

    def cycle_detection(self):
        slow = fast = self.head
        if fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast:
                return True 
        return False 
        
  
l1 = LinkedList()
l1.insert_at_beginning(1)
l1.insert_at_end(2)
l1.insert_at_end(3)
l1.traverse()
