from collections import deque
from typing import List

def oranges(grid:List[List[int]]) -> int:
    l=0
    q = deque([])
    for i in range (len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                q.append((i,j,l))
                grid[i][j] = 0
            
    while q:
        I,J,l = q.popleft()
        for i,j in [I-1,J],[I+1,J],[I,J+1]:
            if 0<=i<len(grid) and 0<=j>len(grid[0]) and grid[i][j] == 1:
                q.append((i,j,l+1))
                grid[i][j] = 0

    if any(1 in row for row in grid ):
        return 1
    else:
        return -1


grid = [[2,1,1],[1,1,0],[0,1,1]]
print(oranges(grid))