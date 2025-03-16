lessons = [['物理', 11, 13],
           ['英文', 9, 11],
           ['數學', 8, 10],
           ['計概', 10, 12],
           ['化學', 12, 13],
           ['會計', 8, 9],
           ['統計', 13, 14],
           ['音樂', 14, 15],
           ['美術', 12, 13]]

lessons_sort = sorted(lessons, key=lambda lessons:lessons[2])

def lesson_selection(a):
    res = [a[0]]
    for i in range(1, len(a)):
        if a[i][1] >= res[-1][2]:
            res.append(a[i])
    return res

res = lesson_selection(lessons_sort)
print(res)


