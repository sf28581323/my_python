a = [6, 1, 5, 7, 3, 9, 4, 8]

def merge(left, right):
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res = res + left + right
    return res

def mergesort(lists):
    if len(lists) <= 1:
        return lists
    mid = len(lists)//2
    left = mergesort(lists[:mid])
    right = mergesort(lists[mid:])
    return merge(left,right)


def search(number, des):
    low = 0
    upper = len(number) - 1
    while low <= upper:
        mid = (low + upper) // 2 
        if number[mid] < des:
            low = mid + 1
        elif number[mid] > des:
            upper = mid - 1
        else:
            return mid
    return -1

b = mergesort(a)
print(b)

find1 = search(b, 2)
print("找到數值 2 於索引 " + str(find1) if find1 >= 0 else "2 不存在於數列中")

find2 = search(b, 8)
print("找到數值 8 於索引 " + str(find2) if find2 >= 0 else "8 不存在於數列中")  

