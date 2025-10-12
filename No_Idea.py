n = input().split()
lst = input().split()

happiness = 0

a = input().split()
b = input().split()

for i,x in enumerate(lst):
    lst[i] = int(x)

for i,x in enumerate(a):
    a[i] = int(x)

for i,x in enumerate(b):
    b[i] = int(x)

a = set(a)
b = set(b)

for x in lst:
    if x in a:
        happiness += 1
    elif x in b:
        happiness -= 1

print(happiness)

