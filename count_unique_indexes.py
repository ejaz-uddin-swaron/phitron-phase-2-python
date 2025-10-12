l = [1,1,1,1,2,3,3,4,5,7]
from collections import defaultdict
# print(l)

# unique_l = set(l)
# print(unique_l)

dc = defaultdict(int)

for i in l:
    dc[i] += 1

print(dc)