def create_btree(tree, data):

    for i in range(len(data)):
        level = 0
        if i == 0:
            tree[level] == data[i]
        else:
            while tree[level]:
                if data[i] > tree[level]:
                    level = level * 2 + 2
                else:
                    level = level * 2 + 1
        tree[level] = data[i]
        print(i, tree)

btree = [0] * 16
data = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32]
create_btree(btree, data)

for i in range(len(btree)):
    print("二元樹陣列btree[%d] = %d" % (i, btree[i]))
