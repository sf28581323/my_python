class Node:
    def __init__(self):
        self.data = 0
        self.next = None

top = None
length = 0

def isEmpty():
    global top

    if(top == None):
        return True
    else:
        return False

def push(data):
    global top
    global length
    
    new_add_node = Node()
    new_add_node.data = data
    new_add_node.next = top
    top = new_add_node
    length += 1

def pop():
    global top

    if isEmpty():
        print('目前為空堆疊')
        return -1
    else:
        ptr = top
        top = top.next
        temp = ptr.data
        print(temp)
        return temp

push('漢堡')
push('薯條')
push('可樂')
push('炸雞')
print(length)
pop()
pop()
pop()
pop()

