import re
import numpy as np

with open('input.txt') as f:
    text = f.readlines()
    text = [[c for c in line if c != '\n'] for line in text]
    text = np.array(text)

total = 0
# Check rows
for row in text:
    total += ''.join(row).count('XMAS')
    total += ''.join(row[::-1]).count('XMAS')
for col in text.T:
    total += ''.join(col).count('XMAS')
    total += ''.join(col[::-1]).count('XMAS')
m, n = text.shape[0], text.shape[1]
for diag in [np.diagonal(text, offset) for offset in range(-m + 1, n)] + [np.diagonal(np.flip(text, axis=1), offset) for offset in range(-m + 1, n)]:
    total += ''.join(diag).count('XMAS')
    total += ''.join(diag[::-1]).count('XMAS')

print(total)

# Part two
total2 = 0
As = np.argwhere(text == 'A')
for x, y in As:
    if 0 < x < m-1 and 0 < y < n-1:
        top_left = text[x-1, y-1]
        bot_left = text[x+1, y-1]
        top_right = text[x-1, y+1]
        bot_right = text[x+1, y+1]
        compl = {'S':'M', 'M':'S'}
        if compl.get(top_left) == bot_right and compl.get(bot_left) == top_right:
            total2 += 1
            
print(total2)

# print(len(re.findall('XMAS', text)))