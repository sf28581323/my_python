from pprint import pprint
maze = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1]
       ]
directions = [
              lambda x, y: (x-1, y),
              lambda x, y: (x+1, y),
              lambda x, y: (x, y-1),
              lambda x, y: (x, y+1),
             ]
def maze_solve(x, y, goal_x, goal_y):
    maze[x][y] = 2
    stack = []
    stack.append((x, y))
    print('迷宮開始')
    while (len(stack) > 0):
        cur = stack[-1]
        if cur[0] == goal_x and cur[1] == goal_y:
            print('目前位置 :', cur)
            print('抵達出口')
            return True
        for dir in directions:
            next = dir(cur[0], cur[1])
            if maze[next[0]][next[1]] == 0:
                print('目前位置 :', cur)
                stack.append(next)
                maze[next[0]][next[1]] = 2
                break
        else:
            maze[cur[0]][cur[1]] = 3
            print('目前位置 :', cur)
            stack.pop()
    else:
        print('沒有路徑')
        return False
maze_solve(1, 1, 4, 4)
pprint(maze)
