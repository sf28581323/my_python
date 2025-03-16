def postorder(ptr):
    if ptr != None:
        postorder(ptr.left)
        postorder(ptr.right)
        print('[%2d]' %ptr.data, end=' ')

def preorder(ptr):
    if ptr != None:
        print('[%2d]' %ptr.data, end=' ')
        preorder(ptr.left)
        preorder(ptr.right)

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

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

tree = Node()
datas = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32]
for d in datas:
    tree.insert(d)
print("前序走訪為:")
preorder(tree)
print(' ')
print("後序走訪為:")
postorder(tree)
