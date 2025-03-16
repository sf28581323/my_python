class Node():
    def __init__(self, data=None):
        self.data=data
        self.next=None

class Linked_list():

    def __init__(self):
        self.head=None

    def print_list(self):
        ptr=self.head
        while ptr:
            print(ptr.data)
            ptr=ptr.next
            
    def search5(self):
        current = self.head 
        count = 0
        while(current is not None): 
            if current.data == 5 :
                count += 1
            current = current.next
        if count == 0 :
                print('5不存在')
        if count != 0 :
                print('5存在')

    def search15(self):
        current = self.head 
        count = 0
        while(current is not None): 
            if current.data == 15 :
                count += 1
            current = current.next
        if count == 0 :
                print('15不存在')
        if count != 0 :
                print('15存在')

    def search20(self):
        current = self.head 
        count = 0
        while(current is not None): 
            if current.data == 20 :
                count += 1
            current = current.next
        if count == 0 :
                print('20不存在')
        if count != 0 :
                print('20存在')
    

    def count(self, search_for): 
        current = self.head 
        count = 0
        while(current is not None): 
            if current.data == search_for: 
                count += 1
            current = current.next
        return count
 
        
link=Linked_list()
link.head=Node(5)
n2=Node(15)
n3=Node(15)
link.head.next=n2
n2.next=n3
link.search5()
link.search15()
link.search20()
print('5的出現次數為'+str(link.count(5)))
print('15的出現次數為'+str(link.count(15)))
print('20的出現次數為'+str(link.count(20)))
