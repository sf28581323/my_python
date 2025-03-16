class list_node:
    def  __init__(self):
        self.val = 0
        self.next = None

head = [list_node]*5

new_node = list_node()

data = [[1, 2], [2, 1], [2, 3], [2, 4], [4, 3], [4, 1]]

print('圖形的鄰接串列內容:')
print('------------------------')

for i in range(1, 5):
    head[i].val = i
    head[i].next = None

    print('頂點 %d =>' %i, end = '')
    ptr = head[i]

    for j in range(6):
        if data[j][0] == i:
            new_node.val = data[j][1]
            new_node.next = None

            while ptr != None:
                ptr = ptr.next
            ptr = new_node

            print('[%d] ' %new_node.val, end = '')
    print()
