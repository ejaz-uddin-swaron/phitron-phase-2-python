useless = int(input())

num = list(map(int, input().split()))

if useless == 1:
    print(num[0], end=" ")
    print(num[0])

    exit()

smallest = min(num)
largest = max(num)

ans = list(filter(lambda x: x == smallest or x == largest, num))

ans.sort()

print(ans[0], end=" ")
print(ans[1])
