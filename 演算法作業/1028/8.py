class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class Double_linked_list():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def print_list1(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def print_list2(self):
        ptr = self.tail
        while ptr:
            print(ptr.data)
            ptr = ptr.prev

link = Double_linked_list()
link.head = Node('Sun')
n2 = Node('Mon')
n3 = Node('Tues')
n4 = Node('Wed')
n5 = Node('Thur')
n6 = Node('Fri')
link.tail = Node('Sat')
link.head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = link.tail
link.print_list1()
print('')
link.tail.prev = n6
n6.prev = n5
n5.prev = n4
n4.prev = n3
n3.prev = n2
n2.prev = link.head
link.print_list2()
