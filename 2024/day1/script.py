# A less verbose functional solution
import numpy as np; print(sum(map(lambda x: abs(x[0] - x[1]), np.sort(np.array(list(map(str.split, open('day1/input.txt').readlines()))).astype(int), axis=0))))
