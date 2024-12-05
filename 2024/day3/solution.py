import re

def q1(text:str):
    muls:list[str] = re.findall(pattern=r'mul\([0-9]+,[0-9]+\)', string=text)
    prod = lambda x: int(x[0])*int(x[1])
    muls = map(lambda mul: prod(mul.lstrip('mul(').rstrip(')').split(',')), muls)
    return sum(muls)
    
def q2(text:str):
    dos = [q1(do.split("don't()")[0]) for do in text.split('do()')]
    print(dos)
    return sum(dos)

with open("input.txt") as f:
    text = f.read()
print(q2(text))