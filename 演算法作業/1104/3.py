class Node: 

    def __init__(self, data): 
        self.data = data 
        self.next = None 
        self.prev = None 
                 
class Queue: 
   
    def __init__(self): 
        self.head = None
        self.last = None
           
    def enqueue(self, data): 
        if self.last is None: 
            self.head = Node(data) 
            self.last = self.head 
        else: 
            self.last.next = Node(data) 
            self.last.next.prev=self.last 
            self.last = self.last.next
               
    def dequeue(self): 
   
        if self.head is None: 
            return None
        else: 
            temp = self.head.data 
            self.head = self.head.next
            self.head.prev = None
            return temp

    def printqueue(self): 
           
        temp=self.last 
        while temp is not None: 
            print(temp.data) 
            temp=temp.prev
            
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.printqueue()
