import numpy as np

with open('test.in') as f:
    lab = f.read().splitlines()
    
def q1(lab) -> int:
    lab = np.array([list(row) for row in lab])
    print(lab)
    guard = np.argwhere(lab == '^')[0]
    direction = (-1, 0)
    print(direction)
    rotate = np.array([[0, -1], [1, 0]])
    print(direction @ rotate)
    m, n = lab.shape[0], lab.shape[1]
    print(m, n)
    count = 0
    while True:
        # Move the guard
        x, y = guard
        lab[x, y] = 'X'
        print(x, y)
        nx, ny = x + direction[0], y + direction[1]
        
        if nx in range(m) and ny in range(n):
            if lab[nx, ny] == '#':
                # Rotate direction
                direction @= rotate
            else:
                guard = nx, ny
                count += 1
        else:
            break
    print(lab)
    return len(np.argwhere(lab == 'X'))
        
def q2(lab):
    print("Question 2")
    lab = np.array([list(row) for row in lab])
    route = lab.copy()
    guard = np.argwhere(lab == '^')[0]
    og = guard.copy()
    ds = np.full(lab.shape, 0, dtype='i, i') # Store direction traversed at location
    direction = np.array([-1, 0]) # Moves up initially
    rotate = np.array([[0, -1], [1, 0]]) # Rotation matrix by +90deg
    m, n = lab.shape
    count = 0
    while True:
        # Move the guard
        x, y = guard
        if lab[x, y] == '.':
            lab[x, y] = '-' if (direction[0] == 0) else '|'
        nx, ny = x + direction[0], y + direction[1]
        
        if nx in range(m) and ny in range(n):
            if lab[nx, ny] == '#':
                # Rotate direction
                lab[x, y] = '+'
                direction @= rotate
            else:
                guard = nx, ny
                count += 1
        else:
            break
        
    print(lab)
    return len(np.argwhere(lab == 'X'))
    

# print(q1(lab))
print(q2(lab))