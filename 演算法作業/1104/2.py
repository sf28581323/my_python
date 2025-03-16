class food:
    def __init__(self):
        self.name = ' '  * 20
        self.next = None

head = None
rear = None
length = 1

def enqueue (name):
    global head
    global rear
    global length

    new_data = food()
    new_data.name = name

    if rear == None:
        head = new_data
    else:
        rear.next = new_data
        length += 1

    rear = new_data
    new_data.next = None
    
    
def dequeue ():
    global head
    global rear

    if head == None:
        print('佇列為空!')
    else:
        print(head.name)
        head = head.next

enqueue('漢堡')
enqueue('薯條')
enqueue('可樂')
enqueue('炸雞')
print(length)
dequeue()
dequeue()
dequeue()
dequeue()
