class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

def inorder(ptr):
    if ptr != None:
        inorder(ptr.left)
        print('[%2d]' %ptr.data, end=' ')
        inorder(ptr.right)

tree = Node()
datas = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32]
for d in datas:
    tree.insert(d)
inorder(tree)
