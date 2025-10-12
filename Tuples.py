n = input()
num = input().split()

for i,x in enumerate(num):
    num[i] = int(x)

num = tuple(num)

ans = hash(num)
print(ans)