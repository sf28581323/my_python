MAX_SIZE = 10

queue = [0] * MAX_SIZE

head = None
rear = 0
item1 = 'Grape'
item2 = 'Mango'
item3 = 'Apple'

def enqueue1(item1):
    global rear
    global MAX_SIZE
    global queue

    if rear == MAX_SIZE-1:
        print('佇列已滿')
    else:
        queue[rear] = item1
        rear += 1

def enqueue2(item2):
    global rear
    global MAX_SIZE
    global queue

    if rear == MAX_SIZE-1:
        print('佇列已滿')
    else:
        queue[rear] = item2
        rear += 1

def enqueue3(item3):
    global rear
    global MAX_SIZE
    global queue

    if rear == MAX_SIZE-1:
        print('佇列已滿')
    else:
        queue[rear] = item3
        rear += 1

enqueue1(item1)
enqueue2(item2)
enqueue3(item3)
print(queue)
print(MAX_SIZE)
