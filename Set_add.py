n = int(input())
ans = set()

while n != 0:
    s = input()
    ans.add(s)

    n -= 1

print(len(ans))