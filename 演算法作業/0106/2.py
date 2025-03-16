from pprint import pprint
maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
       ]
directions = [
              lambda x, y: (x-1, y),
              lambda x, y: (x+1, y),
              lambda x, y: (x, y-1),
              lambda x, y: (x, y+1),
             ]
print('迷宮圖形如下 :')
pprint(maze)
x, y = map(int,input('請輸入迷宮入口 x, y : ').split(', '))
goal_x, goal_y = map(int,input('請輸入迷宮出口 x, y : ').split(', '))
def maze_solve(x, y, goal_x, goal_y):
    maze[x][y] = 2
    stack = []
    stack.append((x, y))
    print('迷宮開始')
    while (len(stack) > 0):
        cur = stack[-1]
        if cur[0] == goal_x and cur[1] == goal_y:
            print('抵達出口')
            return True
        for dir in directions:
            next = dir(cur[0], cur[1])
            if maze[next[0]][next[1]] == 0:
                stack.append(next)
                maze[next[0]][next[1]] = 2
                break
        else:
            maze[cur[0]][cur[1]] = 3
            stack.pop()
    else:
        print('沒有路徑')
        return False
maze_solve(x, y, goal_x, goal_y)
pprint(maze)
