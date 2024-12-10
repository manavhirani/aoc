def q1(data):
    print(data)
    blocks = []
    for i, d in enumerate(data):
        d = int(d)
        blocks += [i//2]*d if i%2 == 0 else [None]*d
    
    b = len(blocks)
    l, r = 0, b - 1
    
    while l < r:
        while blocks[l] != None and l < r: l += 1
        while blocks[r] == None and l < r: r -= 1
        blocks[l] = blocks[r]
        blocks[r] = None
        l += 1
        r -= 1
    
    print([block for block in blocks if block])
    return sum([pos*block for pos, block in enumerate(blocks) if block != None])

def q2():
    pass

def run():
    data = open('test.in').read()
    result = q1(data)
    print(result, 1928)
    
    data = open('input.in').read()
    result = q1(data)
    print(result)
    
    
run()