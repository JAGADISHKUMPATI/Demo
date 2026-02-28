Hello World Ok
from functools import reduce
arr = [12, 3, 4, 15]
ans = reduce(lambda a, b: a + b, arr)
print('Sum:', ans)
