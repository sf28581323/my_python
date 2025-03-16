MAX_SIZE = 20

stack = [0] * MAX_SIZE

top = 0

def push(data):
    global top
    global MAX_SIZE
    global stack

    if top >= MAX_SIZE-1:
        print('堆疊已滿，無法再加入')
        return None
    else:
        top += 1
        stack[top] = data

def pop():
    global top
    global stack

    if isEmpty():
        print('堆疊為空')
        return None
    else:
        print(stack[top])
        top -= 1
        return stack[top+1]

def isEmpty():
    if top == -1:
        return True
    else:
        return False

push(1)
push(2)
push(3)
push(4)
push(5)
push(6)
push(7)
pop()
pop()
pop()
pop()
pop()
pop()
pop()
