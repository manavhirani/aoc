import numpy as np
from collections import defaultdict, deque

# Backtrack to 0s, maintain a map of mxn with storing in dp array

def q1(data: str):
    lines = data.splitlines()
    heights = np.array([list(line) for line in lines], dtype=int)
    dp = defaultdict(set)
    m, n = heights.shape
    nines = np.argwhere(heights == 9)

    print(heights)
    print(dp)
    print(nines)
    
    def inbounds(x, y):
        return x in range(m) and y in range(n)

    for nine in nines:
        p, q = nine
        queue = [nine]
        while queue:
            x, y = queue.pop()
            height = heights[x, y] - 1
            dp[(x, y)].add((p, q))
            nbs = ((0, 1), (1, 0), (0, -1), (-1, 0))
            for dy, dx in nbs:
                nx, ny = x + dx, y + dy
                if inbounds(nx, ny) and heights[nx, ny] == height:
                    queue.append((nx, ny))
        
    print(dp)
    total = 0
    for zero in np.argwhere(heights == 0):
        total += len(dp[tuple(zero)])
    print(total)

def q2(data: str):
    
    lines = data.splitlines()
    heights = np.array([list(line) for line in lines], dtype=int)
    dp = np.zeros_like(heights)
    m, n = heights.shape
    nines = np.argwhere(heights == 9)

    print(heights)
    print(dp)
    print(nines)
    
    def inbounds(x, y):
        return x in range(m) and y in range(n)

    for nine in nines:
        print(f"At nine: {nine}")
        p, q = nine
        dp[p, q] = 1
        queue = [(p, q)]
        while queue:
            x, y = queue.pop(0)
            height = heights[x, y] - 1
            nbs = ((0, 1), (1, 0), (0, -1), (-1, 0))
            for dy, dx in nbs:
                nx, ny = x + dx, y + dy
                if inbounds(nx, ny) and heights[nx, ny] == height:
                    dp[nx, ny] += 1
                    queue.append((nx, ny))
        
    print(dp)
    total = 0
    for zero in np.argwhere(heights == 0):
        total += dp[tuple(zero)]
    print(total)

data = open("./input.in").read()
q1(data)
q2(data)