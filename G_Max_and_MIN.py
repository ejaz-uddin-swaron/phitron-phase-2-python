useless = input()
num = list(map(int, input().split()))

smallest = min(num)
largest = max(num)

filtered = list(filter(lambda x: x != smallest and x != largest, num))

print(filtered)
